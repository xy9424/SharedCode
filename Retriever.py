from github import Github
import Reviewer
import EntityAnalyzer
import Reporter

# Authenticate with GitHub API using personal access token <personal_access_token>
g = Github('')

# Get the repository
# <owner>/<repo_name>
repo = g.get_repo('')

# Get all the pull requests
pull_requests = repo.get_pulls()

# Loop over the pull requests and print the title and body
for pull_request in pull_requests:
    print('Title:', pull_request.title)
    print('Body:', pull_request.body)
    print('---')
    # Get source code from the pull request
    source_code = Reviewer.get_source_code(pull_request)

    # Extract tech stack and library information from the source code
    tech_stack_libs = EntityAnalyzer.extract_entities(source_code)

    # Get the comments on the pull request
    comments = Reviewer.get_review_comments(pull_request)

    # comment scores
    comment_scores = {}

    # Loop over the comments and print the body
    for comment in comments:
        print(comment.body)
        print('---')
        comment_scores[comment] = EntityAnalyzer.analyze_entities(comment, tech_stack_libs)
        print(comment_scores[comment])

    final_report = Reporter(comment_scores)
    final_report.print_comment_score()