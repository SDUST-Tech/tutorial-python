# 任务2: 爬虫的简单实用
## 一. 任务详情:
### 1. 子任务1 
爬取`http://192.168.119.211/JudgeOnline/contestrank.php?cid=3476` 网页，保存下榜单信息为csv格式，具体格式如下：

```
Rank,User,Nick,Marked,Solved,Mark,A,B,C,D,E,F
1,201601060928,wzh,6,6,99.55,99 (1),99 (1),100 (1),100 (2),100 (1),100 (2)
``` 

### 2. 子任务2
在子任务1的基础上，爬取`软件工程18`的全部实验成绩榜单，并整理出如下数据:
```
User,Nick,Mark-1,Mark-2, Mark-3,...
201601060928,wzh,98,98.5,98.3,98.6,...
```
如上所示，假如共有八次实验，则对于每个人，记录下八次的总成绩

### 3. 子任务3
在子任务2的基础上，求出每个人所有实验平均总成绩，并进行排名
### 4. 子任务4
在子任务3的基础上，试图用面向对象去改写原有的代码
## 二. 提交说明:
使用git提交代码到此目录，命名格式如:`软件16-2-wzh.py`

## 三. 提示
详见[tip.md](tip.md)  
**允许多次提交**
