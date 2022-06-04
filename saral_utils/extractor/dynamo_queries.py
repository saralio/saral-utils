
from dataclasses import dataclass


@dataclass
class DynamoQueries:
    """Predefined queries for some of the common use cases. 
    """

    # for R programming related questions
    r_prog_que_key_cond_expr = 'topic = :topic'
    r_prog_que_filter_expr = 'contains (tags, :tag)'
    r_prog_que_attr_values = {
        ':topic': {'S': 'Programming'},
        ':tag': {'S': 'R'}
    }

    # for python programming questions
    py_prog_que_key_cond_expr = 'topic = :topic'
    py_prog_que_filter_expr = 'contains (tags, :tag)'
    py_prog_que_attr_values = {
        ':topic': {'S': 'Programming'},
        ':tag': {'S': 'Python'}
    }

    # for data science questions
    ds_que_key_cond_expr = 'topic = :topic'
    ds_que_filter_expr = None
    ds_que_attr_values = {
        ':topic': {'S': 'Data Science'}
    }
