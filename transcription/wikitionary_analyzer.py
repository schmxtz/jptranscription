import json
# output_file = open('output.json', 'w')
# output = {}
# with open(file='C:/Users/Philipp Schmitz/Downloads/de-extract.jsonl/de-extract.jsonl', encoding='UTF-8') as file:
#     while line := file.readline():
#         json_obj = json.loads(line.rstrip())
#         if json_obj.get('lang_code') == 'de':
#             if json_obj.get('sounds'):
#                 if len(json_obj.get('sounds')) > 0:
#                     if json_obj.get('sounds')[0].get('ipa'):
#                         if output.get(json_obj.get('word').lower()):
#                             output[json_obj.get('word').lower()]['ipa'].append(json_obj.get('sounds')[0].get('ipa'))
#                             output[json_obj.get('word').lower()]['pos'].append(json_obj.get('pos'))
#                         else:
#                             output[json_obj.get('word').lower()] = {'ipa': [json_obj.get('sounds')[0].get('ipa')], 'pos': [json_obj.get('pos')]}
#
# json.dump(output, output_file)

output_file = open('transcription/output.json')
output = json.load(output_file)
print(output['Weltschmerz'.lower()])

