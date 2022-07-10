from typing import List, Dict

def normalize_options(options: List) -> List[Dict[str, str]]:
    """normalizes a dictionary from dynamodb, specific to options

    Args:
        options (List[str]): options of a question from table `saral-questions`

    Returns:
        List[Dict[str, str]]: a list with normalized options in dictonary format. Of the form [{'is_correct':..., 'text':..., 'image_path_exists':...}]
    """    
    flat = []
    for option in options:
        opt = {}
        option = option['M']
        opt['is_correct'] = option['correct']['BOOL']
        opt['text'] = option['text']['S']
        opt['image_path_exist'] = True if 'S' in option['imagePath'].keys() else False

        flat.append(opt)
    return flat

def image_exist(question: Dict) -> bool:
    """for a given question from `saral-questions` table check if the question has any image associated with it whether in question or in option

    Args:
        question (Dict): question data

    Returns:
        bool: True if image exist either in question text or in options otherwise False
    """
    que_image_exist = True if 'L' in question['questionImagePath'].keys(
    ) else False

    options = question['options']['L']
    flatten_option = normalize_options(options)
    opt_image_exist = any([True for opt in flatten_option if opt['image_path_exist']])

    if que_image_exist or opt_image_exist:
        return True
    else:
        return False