import jieba
txt = open("hlm.txt","r",encoding = 'utf-8').read()
excludes = {"什么","一个","我们","那里","如今","你们","说道","起来","姑娘","这里","出来","他们","众人","自己","039","&#","一面","只见","两个","怎么","没有","不是","不知",
           "听见","这个","这样","进来","咱们","就是","东西","告诉","回来","袭人","只是","大家","只得","丫头","这些","不敢","出去","所以","不过","不好","一时","鸳鸯","姐姐",
           "过来","不能","心里","银子","如此","答应","今日","几个","二人","还有","只管","一回","说话","这么","那边","这话","外头","打发","自然","今儿","罢了","那些","小丫头",
           "妹妹","屋里","如何","听说","问道","知道","太太","的话","人家","媳妇","看见","家里","不用","家里","一声","不得","一句","原来","这会子","到底","进去","姊妹","过去",
           "方才","回去","别人","连忙","心中","哥哥","婆子","不成","丫鬟","里头","还是","小厮","只有","一件","明白","身上","有人","起身","已经","一日","那个","于是","果然",
            "分节","阅读","这是","越发","喜欢","怎么样","瞧瞧","谁知","难道","跟前","不必","只怕","吩咐","怎么样"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == '林黛玉' or word == '黛玉道' or word == '林姑娘':
        rword = '黛玉'
    elif word == '凤姐儿':
        rword = '凤姐'
    elif word == '老太太' or word == '奶奶':
        rword = '贾母'
    elif word == '王夫人' or word == '邢夫人':
        rword = '夫人'
    elif word == '薛姨妈':
        rword = '薛姨'
    elif word == '宝':
        for i in range(len(words)):
            if words[i-1] == '宝' and words[i] == '姑娘':
                rword = '宝钗'
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    if word in counts:
        del(counts[word])
items = list(counts.items())
items.sort(key = lambda x:x[1] , reverse = True)
for i in range(20):
    word, count = items[i]
    print("{:<12}{:>5}".format(word,count))
