class Parse:

    def __init__(self, prepositions, delimiter):
        self.prepositions = prepositions
        self.preposition_split_sentences = {prep: [] for prep in
                                            self.prepositions}
        self.delimiter = delimiter

    def _parse_raw_sentences(self):
        counter = 0
        with open("RAW_SENTENCES", 'r') as file_reader:
            for line in file_reader:
                if '\t' in line:
                    line = line[:line.index('\t')]
                for preposition in self._get_substring_propositions():
                    if preposition in line.lower():
                        splited_line = tuple(line.lower().split(preposition))
                        if len(splited_line) != 2 or len(
                                splited_line[0]) < 2 or len(
                                splited_line[1]) < 2:
                            # todo - perhaps limit to longer sentences?
                            print(line)
                            counter += 1
                            continue

                            # in the corpus of 3000 sentences,
                            # this has occurred once with the sentence:
                            # """ " But "Storm Trooper" is not even bad enough
                            # to make it to the list of wonderfully terrible
                            # movies"""

                        self.preposition_split_sentences[
                            preposition[1:-1]].append(
                            splited_line)
        print(counter)

    def extract_preposition_sentences(self):
        self._parse_raw_sentences()
        list_of_files = []
        for prep in self.preposition_split_sentences:
            list_of_files.append(prep + "_sentences")
            with open(list_of_files[-1], 'w') as writer:
                for tup in self.preposition_split_sentences[prep]:
                    writer.write(tup[0] + self.delimiter + tup[1] + "\n")
        return list_of_files

    def _get_substring_propositions(self):
        substrings = []
        for prop in self.prepositions:
            substrings.append(" " + prop + " ")
            substrings.append("," + prop + " ")
            substrings.append(" " + prop + ",")
            substrings.append("," + prop + ",")
            substrings.append("." + prop + " ")
        return substrings
