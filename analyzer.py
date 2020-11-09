import nltk
import stanza
import matplotlib.pyplot as plt
import json
import os
import string
import mpld3
from RUNNING_VARIABLES import *

FIRST_TIME = False


class Analyzer:
    FUNCTION_POS = 0
    KWD_POS = 1
    STRETCHING_FUNC = 2

    def __init__(self, list_of_files):
        self._print_log("starting Analyzer initialization")
        self.list_of_files = list_of_files
        self.sentiment_modules = {}
        self.initialize_modules()
        self.coords = {}
        self._analysis_done = False
        self._print_log("finished Analyzer initialization")
        self.plot_colors = ['red', 'blue', 'green', 'purple']

    def _print_log(self, msg):
        if PRINT_LOGS:
            print(msg)

    @classmethod
    def _get_sid(cls):
        if FIRST_TIME:
            nltk.download('vader_lexicon')
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        return SentimentIntensityAnalyzer()

    @classmethod
    def clean(cls, word):
        if not word:
            return word  # nothing to strip
        for start, c in enumerate(word):
            if c.isalnum():
                break
        for end, c in enumerate(word[::-1]):
            if c.isalnum():
                break
        return word[start:len(word) - end] + "."

    def plot(self):
        if not self._analysis_done:
            print("Warning! you must first analyze before plotting! ")
            return

        self._print_log("starting plotting")

        fig = self._plot_main_figure()

        if DISPLAY_MAIN_IMAGE:
            fig.show()

        if UPDATE_SHOWN_IMAGE:
            self._print_log("saving fig")
            mpld3.save_html(fig,
                            os.path.join('plots',
                                         'preposition_Sentiment_graphs.html'))
            fig.savefig(
                os.path.join('plots', 'preposition_Sentiment_graphs.png'))

        if SHOW_INTERACTIVE_IMAGE:
            mpld3.show()

        if PLOT_INDIVIDUAL_PREPOSITION_MODULE_PLOTS:
            self._plot_individual_plots()

        self._print_log("finised plotting")

    def _plot_main_figure(self):
        fig, all_plots = plt.subplots(len(self.list_of_files),
                                      len(self.sentiment_modules))
        fig.suptitle(
            "Sentiment of first vs second part of clause, parted  by Prepositiosn")

        for mod_idx, module in enumerate(self.sentiment_modules):
            all_plots[0, mod_idx].set_title(module)
            for prop_idx, file_name in enumerate(self.list_of_files):
                self._update_scatter_plot(all_plots, fig, file_name,
                                          mod_idx, module, prop_idx)
        return fig

    def _update_scatter_plot(self, all_plots, fig, file_name, mod_idx,
                             module, prop_idx):
        color = self.plot_colors[prop_idx % len(self.plot_colors)]
        preposition = self.get_preposition_from_filename(file_name)

        scatter = all_plots[prop_idx, mod_idx].scatter(
            self.coords[file_name][module][0],
            self.coords[file_name][module][1],
            color=color)
        all_plots[prop_idx, mod_idx].grid(which='both', axis='both',
                                          color='grey',
                                          linestyle='solid')
        all_plots[prop_idx, mod_idx].axis(xmin=-5, xmax=5,
                                          ymin=-5, ymax=5)
        all_plots[prop_idx, 0].set_ylabel(
            string.capwords(preposition), fontsize=10, color=color)
        all_plots[prop_idx, 0].yaxis.set_label_position("left")
        tooltip = mpld3.plugins.PointLabelTooltip(
            scatter,
            labels=self.coords[file_name][module][2])
        mpld3.plugins.connect(fig, tooltip)

    def analyze(self):
        self._print_log("starting analyzing")
        if not ANALYZE_DATA_FROM_SCRATCH:
            self.load_coords()
            self._analysis_done = True
            self._print_log("finished analyzing")
            return
        for file in self.list_of_files:
            self.coords[file] = {n: ([], [], []) for n in
                                 self.sentiment_modules.keys()}
            self.iterate_file_sentiment(file)
            with open(os.path.join("sentiments", file + '_sentiments.json'),
                      'w') as f:
                json.dump(self.coords[file], f)
        self._analysis_done = True
        self._print_log("finished analyzing")

    def iterate_file_sentiment(self, file):
        with open(os.path.join("sentences", file), 'r') as reader:
            for line in reader:
                first, sec = line.split(DELIMITER)

                first = self.clean(first)
                sec = self.clean(sec)
                preposition = self.get_preposition_from_filename(file)
                sentence = " ".join([first, preposition, sec])
                for mod_name, module in self.sentiment_modules.items():
                    self.coords[file][mod_name][0].append(
                        self.calc_score(module, first))
                    self.coords[file][mod_name][1].append(
                        self.calc_score(module, sec))
                    self.coords[file][mod_name][2].append(sentence)

    @classmethod
    def calc_score(self, module, sentence):
        return module[self.STRETCHING_FUNC](
            module[self.FUNCTION_POS](sentence)[module[self.KWD_POS]])

    def initialize_modules(self):
        nltk_vader = self._get_sid()
        self.sentiment_modules["nltk"] = (
            nltk_vader.polarity_scores, 'compound', lambda x: x * 5)

        from textblob import TextBlob
        self.sentiment_modules["TextBlob"] = (
            lambda x: TextBlob(x).sentiment, 0, lambda x: x * 5)

        nlp = stanza.Pipeline(lang='en', processors='tokenize,sentiment')
        self.sentiment_modules["stanza"] = (
            lambda x: {'s': nlp(x).sentences[0].sentiment}, 's',
            stanza_normalizer
        )

    def load_coords(self):
        for file in self.list_of_files:
            self.coords[file] = self.get_coords_file(file)

    @staticmethod
    def get_coords_file(file):
        with open(os.path.join("sentiments",
                               file + '_sentiments.json')) as json_file:
            return json.load(json_file)

    def _plot_individual_plots(self):
        plotes = os.listdir("./plots")
        for prop_idx, file_name in enumerate(self.list_of_files):
            preposition = self.get_preposition_from_filename(file_name)
            preposition = preposition.replace(" ", "_")
            if preposition not in plotes:
                os.mkdir(os.path.join("plots", preposition))
        lines_for_readme = []
        for prop_idx, file_name in enumerate(self.list_of_files):
            preposition = self.get_preposition_from_filename(file_name)
            lines_for_readme.append("####" + preposition)
            preposition = preposition.replace(" ", "_")
            for mod_idx, module in enumerate(self.sentiment_modules):
                fig, ax = plt.subplots()
                ax.set_title(
                    "1st vs 2nd sentiment of clause, parted  by '" + preposition + "': " + module)
                plt.xlabel('First clause sentiment value', fontsize=18)
                plt.ylabel('Second clause sentiment value', fontsize=16)
                color = self.plot_colors[prop_idx % len(self.plot_colors)]

                scatter = ax.scatter(self.coords[file_name][module][0],
                                     self.coords[file_name][module][1],
                                     color=color)
                tooltip = mpld3.plugins.PointLabelTooltip(
                    scatter,
                    labels=self.coords[file_name][module][2])
                mpld3.plugins.connect(fig, tooltip)
                file_to_save_suffix = preposition + "_" + module
                file_to_save_suffix = file_to_save_suffix.replace(" ", "_")
                file_dir_save = os.path.join('plots',
                                             preposition,
                                             file_to_save_suffix + ".html")
                mpld3.save_html(fig, file_dir_save)

                lines_for_readme.append(
                    "- [" + preposition + "_" + module +
                    "](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/" + file_to_save_suffix + ".html)")

        with open("preposition_graph_links_for_readme.txt",'w') as writer:
            for line in lines_for_readme:
                writer.write(line+"\n")

    def get_preposition_from_filename(self, file_name):
        return file_name.split("_")[0]


def stanza_normalizer(sentiment):
    # negative: 0
    # neutral: 1
    # positive: 2
    switcher = {0: -3, 1: 0, 2: 3}
    return switcher[sentiment]
