from warnings import warn
import re
# extracts code snippet from a given string

def code(text: str, pattern: str = "(?<=```)(.*?)(?=```)") -> dict:
    """
    for a given text string it extracts the code part from the string. It returns a dictionary
    of the form text and code separately. The returned "text" is without code
    return value: dict
    return value format: {
        "text": the text without code,
        "code": {
            "code_text": code text,
            "language": r|python,
            "sno": 1|2|3... the sno of code snippet among many snippets, 
        }
    }
    """
    matches = re.findall(pattern, text, flags=re.S)

    j = 1
    code_list = []
    for i in range(0, len(matches), 2):

        language = re.search("^ *\w*?\n", matches[i], re.S)
        if language is None:
            language = None
            warn('Language tag not provided to question')
            code = matches[i].strip()
        else:
            language = language.group(0).strip()
            code = re.sub(language, "", matches[i], 1).strip()

        code_list.append(
            {
                "code": code,
                "language": language,
                "sno": j
            }
        )
        j += 1

    text3 = text.replace("```", " ")
    text3 = re.sub(" +", " ", text3)

    return {
        "text": text3,
        "code_info": code_list
    }

if __name__=="__main__":

    text = """
    this is a sample text
    ```
    x = 1
    ```
    another sample text with language tag
    ``` R
    x = 2
    ```

    last tag with language tag
    
    ```python
    x = 3
    ```
    """
    print(code(text=text))
