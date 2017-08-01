## sklearn

全名Scikit-Learn，是基于Python的机器学习模块，基于BSD开源许可证。

数据结构基于Numpy与pandas，数据计算基于Scipy，数据可视化基于matplotlib。

基本功能主要被分为6个部分，分类，回归，数据降维，模型选择，数据预处理

将具体的机器学习分为三个步骤，数据准备与预处理，模型选择与训练，模型验证与参数调优

sklearn包的分词方式是基于空格与标点符号进行分词的（英文）

**文档向量化**

```python
#sklearn.feature_extraction.text.CountVectorizer
CountVectorizer(stop_words,min_df,token_pattern=r"\b\w+\b")
#类用于词频统计由三个参数，默认会去掉长度为1的分词
#stop_words 停用词数组
#min_df 分词最小长度
#token_pattern 分词的正则表达式
```

**TFIDF计算**

```bash
sklearn.feature_extraction.text.TfidfTransformer
#不需要构造参数，使用TfidfTransformer方法把传入的文档向量化矩阵计算为TFIDF矩阵
```

**其它**

```bash
fit_transform() #文档向量化

todense() #获取文档向量化生成的矩阵

vocabulary_ #查看每个列对应的分词

toarray() #转换成矩阵

get_feature_names() #获取单词

numpy.argsort() #间接排序，将数值从小到大返回索引

" ".join(segments) #为了适应sklearn为分词加上空格

```


## 相似文章推荐

**协同过滤推荐**

指利用已有用户群过去的行为或意见，预测当前用户最可能喜欢哪些东西或对哪些东西感兴趣


**余弦相似度**

用向量空间中两个向量夹角的余弦值作为衡量两个个体间差异的大小。余弦值越接近1，就表明夹角越接近0度，也就是两个向量越相似，这个特征也叫做“余弦相似性”

![余弦](assets/markdown-img-paste-20170726113752981.png)

**如何计算余弦相似度**

首先对文章进行分词，将分词去重后形成语料库，统计分词在文章中出现的次数（向量化），生成的向量要严格按照语料库中的顺序进行排序，如果某篇文章不包含某个分词，需要将该位置的值设置为0，最后根据的到的文章的向量按照余弦值的计算公式得出余弦值

```mermaid
graph LR
  分词&去重 --> 语料库;
  语料库 --> 向量化;
```

![计算](assets/markdown-img-paste-20170726120813147.png)


**余弦距离计算**：矩阵中每行之间的距离

```python
sklearn.metrics.pairwise_distances
#matrix 矩阵
#metric="consine" 距离计算公式
```

## 自动摘要

摘要：是全面准确的反映某一文献中心内容的简单连贯的短文，让读者尽快的了解文章的主要内容

自动摘要：是利用计算机自动的从原始文献中提取摘要

**算法步骤**
1. 获取到需要摘要的文章
2. 对该文章进行词频统计
3. 对该文章进行分句
  --根据中文的标点符号，一般我们采用“。”、“？”等进行分句
4. 计算分句与文章之间的余弦相似度
5. 取相似度最高的分句，作为文章的摘要

**文本切割、分句**
```python
#建立子语料库，以该文档和该文档的分句组成
subCorpos = [fileContent] + re.split(
    r'[。？！\n]\s*',
    fileContent
)

```
