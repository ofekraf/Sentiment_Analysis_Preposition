class Parse:

    def __init__(self, prepositions):
        print("starting")
        self.prepositions = prepositions

    def _parse_raw_sentences(self, preposition_split_sentences):
        with open("RAW_SENTENCES", 'r') as file_reader:
            for line in file_reader:
                if '\t' in line:
                    line = line[:line.index('\t')]
                for preposition in self._get_substring_propositions():
                    if preposition in line.lower():
                        splited_line = tuple(line.split(preposition))
                        if len(splited_line) > 2:
                            print(line)
                            continue
                            # in the corpus of 3000 sentences, this has not occured once:
                        preposition_split_sentences[preposition[1:-1]].append(
                            splited_line)

    def extract_preposition_sentences(self):
        preposition_split_sentences = {prep: [] for prep in self.prepositions}
        self._parse_raw_sentences(preposition_split_sentences)
        list_of_files = []
        for prep in preposition_split_sentences:
            list_of_files.append(prep + "_sentences")
            with open(list_of_files[-1], 'w') as writer:
                for tup in preposition_split_sentences[prep]:
                    writer.write(str(tup) + "\n")
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