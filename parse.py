import os
from RUNNING_VARIABLES import *


class Parse:

    def __init__(self, prepositions, delimiter):
        self._log("initializing Parser")
        self.prepositions = prepositions
        self.preposition_split_sentences = {prep: [] for prep in
                                            self.prepositions}
        self.delimiter = delimiter
        self.prepositions_counter = {prep: 0 for prep in
                                     self.prepositions}
        self.discarded_lines = []
        self._log("finished initialization")

    def _parse_raw_sentences(self):
        with open("RAW_SENTENCES", 'r') as file_reader:
            for line in file_reader:
                if '\t' in line:
                    line = line[:line.index('\t')]
                self.parse_line(line)
        self.log_discarded_lines()

    def parse_line(self, line):
        for preposition in self._get_substring_propositions():
            # if len(self.preposition_split_sentences[
            #            preposition[1:-1]]) > 100:
            #     self.prepositions_counter[preposition[1:-1]] += 1
            #     if (self.prepositions_counter[preposition[1:-1]] % 50) != 0:
            #         continue
            if preposition in line.lower():
                splited_line = tuple(line.lower().split(preposition))
                if self._should_dis_regard_line(splited_line):
                    self.discarded_lines.append(line)
                    continue
                self.preposition_split_sentences[
                    preposition[1:-1]].append(
                    splited_line)

    def log_discarded_lines(self):
        with open("discarded_lines.log", 'w') as writer:
            writer.write("amount of discarded lines: {} \n".format(
                len(self.discarded_lines)))
            for line in self.discarded_lines:
                line = line + '\n' if '\n' not in line else line
                writer.write(line)

    def extract_preposition_sentences(self):
        self._log("extracting prepositional sentences")

        self._parse_raw_sentences()

        for prep in self.preposition_split_sentences:
            self._write_results(prep)

            self._log("for preposition {} wrote {} lines".format(prep, len(
                self.preposition_split_sentences[prep])))

        self._log("finished writing prepositional sentences")

    def _write_results(self, prep):
        cur_file = prep + "_sentences"
        temp = self.delimiter
        self.delimiter = " but "
        with open(os.path.join("sentences", cur_file), 'w') as writer:
            for tup in self.preposition_split_sentences[prep]:
                res = tup[0] + self.delimiter + tup[1]
                res = res + '\n' if '\n' not in res else res
                writer.write(res)
        self.delimiter = temp

    def _get_substring_propositions(self):
        substrings = []
        for prop in self.prepositions:
            substrings.append(" " + prop + " ")
            substrings.append("," + prop + " ")
            substrings.append(" " + prop + ",")
            substrings.append("," + prop + ",")
            substrings.append("." + prop + " ")
        return substrings

    def _log(self, param):
        if PRINT_LOGS:
            print(param)

    def _should_dis_regard_line(self, splited_line):
        if len(splited_line) != 2:
            return True
        if len(splited_line[0].split(" ")) < MINIMAL_AMOUNT_OF_WORDS_IN_CLAUSE:
            return True
        if len(splited_line[1].split(" ")) < MINIMAL_AMOUNT_OF_WORDS_IN_CLAUSE:
            return True
        return False