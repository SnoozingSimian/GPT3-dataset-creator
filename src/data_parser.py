"""
{
    'prompt':'[[actions: bla, bloh, bleh]]
              [[emotes: hic, snic, pic]]
              
              Potato: This is a great day to be a vegetable!
              Tomato: I suppose it is, I don't share your enthusiasm though.

              Potato: Why?',    
    'answer':'Tomato: Because I am not a vegetable, I am a fruit!'
}
"""

def parse_data(data: dict) -> dict:
    parsed_data = {}
    
    parsed_data['prompt'] = f"""{data['prompt'].strip()}"""
    if data['emotes'] != "":
       parsed_data['prompt'] = f"""{data['emotes'].strip()}\n""" + parsed_data['prompt'] 
    if data['actions'] != "":
        parsed_data['prompt'] = f"""{data['actions'].strip()}\n""" + parsed_data['prompt']
    
    parsed_data['completion'] = f"""{data['answer'].strip()}"""

    return parsed_data
    