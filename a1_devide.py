import os
from tqdm import tqdm

with open("a1_train_incorr_sentences.txt", "r") as source_data:
        with open( "a1_train_corr_sentences.txt" , "r") as target_data: 
            i = 0
            writecount = 0

            file_incorrect_path = "a1_devide/a1_incorrect_" + str(i) + ".txt"
            file_correct_path = "a1_devide/a1_correct_" + str(i) + ".txt"
            source_sents = []
            target_sents = []
            for source_sent, target_sent in tqdm(zip(source_data, target_data)):

                if writecount == 1000:
                    with open( file_incorrect_path , encoding='utf-8', mode='w') as inf:
                        inf.writelines( source_sents )
                    with open( file_correct_path , encoding='utf-8', mode='w') as cof:
                        cof.writelines( target_sents )
                    writecount = 0
                    i = i + 1
                    file_incorrect_path = "a1_devide/a1_incorrect_" + str(i) + ".txt"
                    file_correct_path = "a1_devide/a1_correct_" + str(i) + ".txt"
                    source_sents = []
                    target_sents = []
                else:
                    source_sents.append(source_sent)
                    target_sents.append(target_sent)
                    writecount = writecount +1
                