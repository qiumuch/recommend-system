# -*- coding: utf-8 -*-
import os
import os.path
import codecs
import numpy
import pandas
import jieba

fileContents = []
for root, dirs, files in os.walk(
    "/root/din/2.3/treeH"
):
    for name in files:
        filePath = os.path.join(root, name)
        f = codecs.open(filePath, 'r')  
        fileContent = f.read()
        f.close()
        fileContents.append(fileContent.lower())

#读取停用词
stopwords = pandas.read_csv(
    "/root/din/2.3/StopwordsEN2.txt", 
     index_col=False
)
#去除停用词中的空格值
stopwords.stopword.str.strip()

#读取COCA语料库
corpus = pandas.read_excel(
    '/root/din/2.3/COCA.xlsx',
    sheetname='20000_words-2'
#    names=['sorti','word']
#    index_col=False
)

#分词后
#fSegStat = segStat[
#    ~segStat.segment.isin(stopwords.stopword)
#]

#分词时
segments = []
for fileContent in fileContents:
    segs = jieba.cut(fileContent)
    for seg in segs:
        if seg not in stopwords.stopword.values and seg in corpus.word.values and len(seg.strip())>1:
            segments.append(seg)


segmentDataFrame = pandas.DataFrame({
    'segment': segments
})

#统计词频
segStat = segmentDataFrame.groupby(
            by="segment"
        )["segment"].agg({
            "jishu":numpy.size
        }).reset_index().sort_values(
            "jishu",
            ascending=False
        )

#导出词频
segStat.to_csv(
    "/root/din/2.3/freq.csv",
    index=False
)

print(segStat[segStat.jishu>1])

