import argparse

from utils.helpers import read_lines, normalize
from gector.gec_model import GecBERTModel

def extract( preds ):
    #tokens = sent.split(" ")
    new_sents = []
    for pred in preds :
        if pred.endswith("||"):
            pred = pred[:-2]
        new_sent = ""
        pred_splite = pred.split("||")
        for pred_token in pred_splite:
            #print(pred)    
            #print(pred_token)
            pred_token = pred_token.split(" ")
            #print(pred_token[6])
            if "$START" in pred_token[6]:
                continue
            if(pred_token[5] == "$KEEP)"):
                #print(tokens)
                #print(int(pred_token[1]))
                #print(pred_token[6])
                new_sent = new_sent + " " + pred_token[6]
            elif(pred_token[5] == "$DELETE)"):  
                continue   
            elif(pred_token[5] == "$REPLACE)"):
                new_sent = new_sent + " " +'[Mask]'
            elif(pred_token[5] == "$APPEND)"):
                new_sent = new_sent + " " + pred_token[6] + " " + '[Mask]'
            else:
                new_sent = new_sent + " " +'[Mask]'
        #print(new_sent)
        new_sents.append(new_sent)
        #print(new_sent)
    return new_sents
        
def predict_for_file(input_file, output_file, model, batch_size=32, to_normalize=False):
    test_data = read_lines(input_file)
    predictions = []
    cnt_corrections = 0
    batch = []
    new_sents = []
    for sent in test_data:
        batch.append(sent.split())
        if len(batch) == batch_size:
            preds = model.handle_batch(batch)
            batch_new_sents = extract( preds  )
            #print( new_sent )
            new_sents.extend( batch_new_sents )
            #cnt_corrections += cnt
            batch = []
    if batch:
        preds = model.handle_batch(batch)
        batch_new_sent = extract( preds  )
        #print( new_sent )
        #predictions.extend(preds)
        new_sents.extend( batch_new_sents )
        #cnt_corrections += cnt

    #result_lines = [" ".join(x) for x in predictions]
    #if to_normalize:
        #result_lines = [ line for line in result_lines]
#     print('outputdick ', args.output_file)
#     print('inputdick ', args.input_file)
#     print('result line ', result_lines)
    with open(output_file, 'w') as f:
        f.write("\n".join(new_sents) + '\n')
    #return cnt_corrections

def predict_for_input(test_data , model, batch_size=32, to_normalize=False):
    batch = []
    new_sents = []
    for sent in test_data:
        batch.append(sent.split())
        if len(batch) == batch_size:
            preds = model.handle_batch(batch)
            batch_new_sents = extract( preds  )
            #print( new_sent )
            new_sents.extend( batch_new_sents )
            #cnt_corrections += cnt
            batch = []
    if batch:
        preds = model.handle_batch(batch)
        batch_new_sents = extract( preds  )
        #print( new_sent )
        #predictions.extend(preds)
        new_sents.extend( batch_new_sents )
    output_str = "\n".join(new_sents) + '\n'
    return output_str
    #with open(output_file, 'w') as f:
        #f.write("\n".join(new_sents) + '\n')
    #return cnt_corrections

def predict_for_UI(input_text):
    # get all paths
    model = GecBERTModel(vocab_path= "model_save/vocabulary",
                         model_paths= ["model_save/model.th"],
                         max_len= 50, min_len= 3,
                         iterations= 5 ,
                         min_error_probability= 0.0 ,
                         lowercase_tokens= 0,
                         model_name= "roberta",
                         special_tokens_fix=1,
                         log=[False],
                         confidence=0,
                         del_confidence=0,
                         is_ensemble=0,
                         weigths=None)
    result = predict_for_input([input_text] , model, 32, False)
    return result

def main(args):
    # get all paths
    result = predict_for_UI(args.text)
    print(result)
    # evaluate with m2 or ERRANT
    print(f"Produced overall ")
    

if __name__ == '__main__':
    # read parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('--text',
                        help='Path to the model file.', nargs='+',
                        required=True)
   
    args = parser.parse_args()
    print(args.text)
    main(args)
