# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

TELEPHONES = 'Rise with the morning You call to me My thoughts are crawling Youre all I see .I wish I could live without you But youre a part of me Wherever I go Youll always be next to me .Fall into the night As I gaze into you Shine so bright Its all I do I wish I could live without you But youre a part of me Wherever I go Youll always be next to me Youll always be next to me Youll always be next to me Youll always be next to me Youll always be next to me'
DARKPARADISE= 'Kiss me hard before you go Summertime sadness I just wanted you to know That, baby, you the best I got my red dress on tonight Dancin in the dark in the pale moonlight Done my hair up real big beauty queen style High heels off Im feelin alive Oh, my God, I feel it in the air Telephone wires above are sizzlin like a snare Honey, Im on fire, I feel it everywhere Nothin scares me anymore Kiss me hard before you go Summertime sadness I just wanted you to know That, baby, you the best I got my red dress on tonight Dancin in the dark in the pale moonlight Done my hair up real big beauty queen style High heels off Im feelin alive Oh my God I feel it in the air Telephone wires above are sizzlin like a snare Honey Im on fire I feel it everywhere Nothin scares me anymore Kiss me hard before you go Summertime sadness I just wanted you to know That, baby, you the best I got that summertime, summertime sadness Su-su-summertime, summertime sadness Got that summertime, summertime sadness Oh, oh-oh-oh-oh Im feelin electric tonight Cruisin down the coast goin' 'bout 99 Got my bad baby by my heavenly side I know if I go, Ill die happy tonight Oh, my God, I feel it in the air Telephone wires above are sizzlin like a snare Honey, Im on fire, I feel it everywhere Nothin scares me anymore Kiss me hard before you go Summertime sadness I just wanted you to know That baby, you the best I got that summertime, summertime sadness Su-su-summertime, summertime sadness Got that summertime, summertime sadness Oh, oh-oh-oh-oh Think Ill miss you forever Like the stars miss the sun in the mornin sky Laters better than never Even if youre gone, Im gonna drive (drive), drive'
FREEFALL = 'Called to the Devil and the Devil did come I said to the Devil, "Devil, do you like drums? Do you like cigarettes, dominoes, rum?" He said, "Only sundown, Sundays, Christmas" Some days end when I need a few friends Now and again, I could never hope to keep them Thought to give friends what I thought that they wanted Never had they needed a good friend as Ive been Dont get me ventin on friends who resent you Cause all youve ever done is been a noose to hang on to They thought was a necklace and reckless They fell into Hell where you both hang with nothing to do but Scratch, kick, let gravity win like Fuck this, let gravity win like You could leave it all behind Even the Devil need time alone sometimes You could let it all go You could let it all go Its called freefall Its called "freefall Called to the Devil and the Devil did come I said to the Devil, "Devil, do you like drums? Do you like cigarettes, dominoes, rum?" He said, "Only sundown, Sundays, Christmas" Some days end when I need a few friends Now and again, I could never hope to keep them Thought to give friends what I thought that they wanted Never had they needed a good friend as Ive been Dont get me ventin on friends who resent you Cause all youve ever done is been a noose to hang on to They thought was a necklace and reckless They fell into Hell where you both hang with nothing to do but Scratch, kick, let gravity win like Fuck this, let gravity win like You could leave it all behind Even the Devil need time alone sometimes You could let it all go you could let it all go Its called Freefall'



# DATA - lyrics


# DATA - mantras
GREEN_LATTERN = 'In brightest day, in blackest night, No evil shall escape my sight. Let those who worship evil\'s might, Beware my power... Green Lantern\'s light!'
JEDI_CODE = 'Emotion, yet peace. Ignorance, yet knowledge. Passion, yet serenity. Chaos, yet harmony. Death, yet the Force.'
SITH_CODE = 'Peace is a lie. There is only Passion. Through Passion, I gain Strength. Through Strength, I gain Power. Through Power, I gain Victory. Through Victory my chains are Broken. The Force shall free me.'

# the input, what we want to encode
def huffman(message:str) -> float:
    message = message.upper()

    # the output, should be all 0's and 1s
    result: str = str()

    # for counting the letter frequencies
    freq: dict = dict() # key  -> a letter
                        # item -> num of occurences

    # for holding the nodes of the huffman tree
    nodes: list = list() 

    # for storing the code for each letter
    coding: dict = dict()   # key  -> a letter
                            # item -> a binary encoding

def huffman(message:str) -> float:
    message = message.upper()

    # the output, should be all 0's and 1s
    result: str = str()

    # for counting the letter frequencies
    freq: dict = dict() # key  -> a letter
                        # item -> num of occurences

    # for holding the nodes of the huffman tree
    nodes: list = list() 

    # for storing the code for each letter
    coding: dict = dict()   # key  -> a letter
                            # item -> a binary encoding

    class Node: # NOT given to students
        weight:int
        letters:str
        left:any
        right:any
    # TODO
   
        def __init__(self, letters= None, weight=None, left=None, right=None ):
            self.weight= weight
            self.letters= letters
            self.left= left
            self.right= right
        
    
## defining operations
### recursively traverses the huffman tree to record the codes
    def retrieve_codes(v: Node, path: str=''):
        if v.letters != None: # if 'TODO': # TODO
            coding[v.letters] = path # TODO
        else:
            retrieve_codes(v.left, path + '0') # TODO
            retrieve_codes(v.right, path + '1')  # TODO

# STEP 1
## counting the frequencies - TODO
    for i in message:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1


# STEP 2
## initialize the nodes - TODO
    nodes =list()
    for letters, count in freq.items():
    #nodes = list()
        nodes.append(Node(letters,count))

# STEP 3 - TODO     
## combine each nodes until there's only one item in the nodes list
    while len(nodes) > 1:
    ## sort based on weight
        nodes.sort(key=lambda x: x.weight, reverse=True)

    ## get the first min
        min_a: Node = nodes.pop()

    ## get the second min
        min_b: Node = nodes.pop()

    ## combine the two
        combined = Node(None,min_a.weight + min_b.weight, min_a, min_b) # TODO

    ## put the combined nodes back in the list of nodes
        nodes.append(combined)

# STEP 4
## reconstruct the codes
    huff_root = nodes[0]
    retrieve_codes(huff_root)
    print(coding)
    
    for i in message:
        result += str(coding[i])
    #result: str = str(coding [i])
    


 # TODO (hint coding[letter] -> code)


# STEP 5
## analyize compression performance
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = (1 - n_encoded_bits / n_original_bits) * 100

    print(f'original: {n_original_bits:^4d} bits')
    print(f'encoded : {n_encoded_bits:^4d} bits')
    print(f'savings : {int(compression_ratio):^4d} % compression')
    return result, coding, compression_ratio


    ## reconstruct the codes

    # STEP 5
    ## analyize compression performance
    #n_original_bits: int = len(message) * 8
    #n_encoded_bits: int = len(result)
    #compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    #return result, coding, compression_ratio

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Stapleton Analyzing Huffman')

MAX_N: int = int(128 * 3 / 2)

# PLOT 1
## POKEMON
data = str = TELEPHONES
ratios: list = list()
for i in range(1, len(data)):
    x = data[0:i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
    min_ratio=min(ratio)
    min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], 
label = f'TELEPHONES (n={len(coding)})',color = 'green',linestyle='dashdot')


## JIGGLE JIGGLE
data: str = DARKPARADISE
ratios: list = list()
for i in range(1,len(data)):
    x= data[0:i]
    compressed, coding, ratio= huffman(x)
    ratios.append(ratio)
    min_ratio = min(ratios)
    min_idx = ratios.index (min_ratio)

plt.plot (ratios [:MAX_N], label = f'DARKPARADISE(n={len(coding)})', color='green', linestyle='dashdot' )


## ALPHABET

data: str = FREEFALL
ratios: list = list()
for i in range(1, len(data)):
    x= data [0:i]
    compressed, coding, ratio = huffman (x)
    ratios.append(ratio)
    min_ratio = min(ratios)
    min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'FREEFALL(n={len(coding)})', color ='blue', linestyle='dashdot')
plt.legend()
plt.gcf().supylabel("compression %")

    
# PLOT 2
plt.subplot(2, 1, 2)

## SITH CODE
data: str = SITH_CODE
ratios: list = list()
for i in range(1, (len_data)):
    x= data[0:i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
    min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'SITH_CODE (n={len(coding)})', color ='red', linestyle='dashdot')


## GREEN LATERN'S OATH
data : str = GREEN_LATTERN
ratios: list = list()
for i in range(1, MAX_N):
    x = data[0:i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
    min_ratio =  min(ratios)
    min_inx= ratios(min_ratio)
    

plt.plot(ratios[:MAX_N], label=f'GREEN_LANTERN(n={len(coding)})', color ='green', linestyle='dashdot')


## JEDI CODE
data: str = JEDI_CODE
ratios: list = list()
for i in range(1, len(data)):
    x= data[0:i]
    compressed, coding,ratio = huffman(x)
    ratios.append(ratio)
    min_ratio= min(ratios)
    min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'JEDI CODE (n={len(coding)})', color ='blue', linestyle='dashdot')

plt.xlabel("length of message")
plt.legend()
plt.show()
    
plt.plot(ratios[:MAX_N], label=f'Abundance (n={len(coding)})', color ='green', linestyle='dashdot')
