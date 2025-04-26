# webshell-framework(wsf)
## 总体架构
该项目作为webshell框架，模仿msf的设计思路和操作方法开发  
主要分为四个部分，分别是基础命令行，生成器，连接器，免杀器(?)  
一个webshell连接设计成一个session  
增加接口能让用户自行开发
## 基础命令行(basic shell)
### 作用
提供基础的命令，刚启动wsf时使用的
### 命令
- about
  - 输出项目基本信息(版本)，作者信息，项目地址等
- list 参数
  - 可选择参数为modules和sessions
    - modules：生成器、连接器、免杀器
    - sessions：连接的webshell
- use 参数
  - 参数为modules
- con 参数
  - 参数为sessionID
- exit
  - 退出程序
- help
  - 帮助
## 生成器(Generator)
### 作用
生成webshell，提供基础的加密
### 命令
- use
- about
- exit
- help
- set 参数
  - url
    - webshell地址
  - pass
    - 密码
## 连接器(Connector)
### 命令
- use
- about
- exit
- help
- con
- list