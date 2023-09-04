
def get_changed_source_code(pull_request):
    # Get the files changed in the pull request
    files = pull_request.get_files()

    # Get the contents of the files
    contents = []
    for file in files:
        if file.status == 'modified':
            contents.append(file.patch)

    # Concatenate the contents into a single string
    source_code = '\n'.join(contents)    
    return source_code

def get_source_code(repo, pull_request):
    # Get the files changed in the pull request
    files = pull_request.get_files()

    # Get the contents of the files
    contents = []
    for file in files:
        if file.status == 'modified':
            source_file = repo.get_contents(file.filename, ref=file.sha)
            contents.append(source_file.decoded_content.decode('utf-8'))

    # Concatenate the contents into a single string
    source_code = '\n'.join(contents)    
    return source_code


def get_review_comments(pull_request):
    # Get the review comments based the pull request
    comments = pull_request.get_review_comments()
    
    return comments
