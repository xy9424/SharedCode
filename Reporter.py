# A data object Reporter to store the score in EntityAnalyzer.py
# The Reporter object can store the score of the comment and the comment itself
# The Reporter object can also store the average score of all comments
# The Reporter object has a function to print the comment and the score
# The Reporter object has a function to print the average score


class Reporter:
    def __init__(self, comment_scores):
        self.comment_scores = comment_scores
        self.average_score = sum(comment_scores.values()) / len(comment_scores)

    # Print each comment and its score
    def print_comment_score(self):
        for comment in self.comment_scores:
            print(comment.body)
            print('---')
            print(self.comment_scores[comment])

    def print_average_score(self):
        print(self.average_score)


