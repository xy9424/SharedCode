import spacy
import Reporter

# Load the English language model for spaCy
nlp = spacy.load('en_core_web_sm')

# Define a function to extract the key libraries and tech stack from the source code
def extract_entities(source_code):
    # Parse the source code using spaCy
    doc = nlp(source_code)
    
    # Extract the entities from the parsed document
    entities = set()
    for ent in doc.ents:
        print (ent.text, ent.label_)
        if ent.label_ in {'ORG', 'PRODUCT', 'TECHNOLOGY'}:
            entities.add(ent.text.lower())
    
    return entities

# Define a function to analyze the entities in the comments
def analyze_entities(comment, entities):
    
    # Parse the comment using spaCy
    comment_doc = nlp(comment.body)
    
    # Extract the mentions of the entity from the comment
    entity_mentions = set()
    for ent in comment_doc.ents:
        for code_entity in entities:
            if ent.text.lower() == code_entity.text.lower() and ent.label_ == code_entity.label_:
                entity_mentions.add(ent.text.lower())
    
    # Update the score for the comment based on the number of entity mentions
    return len(entity_mentions)
    