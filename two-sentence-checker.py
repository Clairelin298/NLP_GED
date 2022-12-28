def check_similar(token_line1s , token_line2s):
    
    #print(token_line2s)
    token_line1s = token_line1s[1:]
    #print(token_line1s)
    token_line1 = token_line1s.split(" ")
    token_line2 = token_line2s.split(" ")
    #print(token_line1)
    #print(token_line2)
    iter = min( len(token_line1) , len(token_line2))
    similar_count = 0
    if ( (len(token_line1) < len(token_line2) -5) or (len(token_line1) > len(token_line2) +5)):
        return False
    for index in range(iter):
        if ( token_line1[index] == token_line2[index] ) :
            similar_count = similar_count + 1
        try:
            if( token_line1[index] == token_line2[index+1] ) :
                similar_count = similar_count + 1
        except Exception as e:
            #print()
            a = 1
        try:
            if( token_line1[index] == token_line2[index-1] ) :
                similar_count = similar_count + 1
        except Exception as e:
            #print()
            a = 1
    # print( str(float(similar_count)/iter) )
    # print( token_line1 )
    # print( token_line2 )
    # if(similar_count > 0):
    #     print(similar_count, iter, similar_count/iter)
    if (similar_count/iter) > 0.8:
        # print(similar_count, iter, similar_count/iter)
        return True
    else:
        return False

def write_parallel( predict_line , origin_line , applie_line):
    with open( "fce-predict-fix.txt", 'a') as predict:
        predict.write( predict_line[1:] )
    with open( "fce-origin-fix.txt", 'a') as origin:
        origin.write( origin_line )
    with open( "fce-applie-fix.txt", 'a') as origin:
        origin.write( applie_line )

def tidy_two_sentence( origin_file_path , pridect_file_path , applied_file_path ):
    with open( pridect_file_path, 'r') as pridect_data:


        pos_in_origin = 0
        origin_file = open( origin_file_path )

        origin_content = origin_file.readlines()

        applie_file = open( applied_file_path )
        applie_content = applie_file.readlines()
        print(len(origin_content))

        for pridect_sent in pridect_data:
            
            temp = pos_in_origin
            # flag = 0
            for check_itr in range( 10000):
                if( temp > len(origin_content)-1 ):
                    break
                else:
                    if( check_similar(pridect_sent , origin_content[temp] ) ):
                        write_parallel( pridect_sent , origin_content[temp] , applie_content[temp] )
                        # flag = 1
                        pos_in_origin = temp + 1
                        break
                    else:
                        temp = pos_in_origin + check_itr
            # if not flag:
                

tidy_two_sentence( "fce-original.txt" , "fce-pridect-result.txt" , "fce-applied.txt")


            
