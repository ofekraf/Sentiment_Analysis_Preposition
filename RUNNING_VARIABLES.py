


#==================Parser====================================
EXTRACT_PREPOSITION_SENTENCES = False
MINIMAL_AMOUNT_OF_WORDS_IN_CLAUSE = 2

#==================Analyzer==================================
RUN_ANALYSER = False
ANALYZE_DATA_FROM_SCRATCH = RUN_ANALYSER and False

#==================Graph======================================
DISPLAY_MAIN_IMAGE = RUN_ANALYSER and True
UPDATE_SHOWN_IMAGE = RUN_ANALYSER and False
SHOW_INTERACTIVE_IMAGE = RUN_ANALYSER and False
PLOT_INDIVIDUAL_PREPOSITION_MODULE_PLOTS = RUN_ANALYSER and True
#==================Logs=======================================
PRINT_LOGS = True

#==================README_DATA=======================================
GET_REPRESENTATIVE_SENTENCES = True
GET_STATISTICS = True
GET_VECTOR_NOTATION = True

#==================Original data==============================
CLEAN_TWEETS = False
CLEAN_MOVIE_LINES = False

#==================Prepositions===============================
DELIMITER = "###---###"
CHECKED_PREPOSITIONS = ['although', 'and yet', 'but', 'even though', 'however', 'therefore']