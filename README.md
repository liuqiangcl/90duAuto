# 90duAuto
1.需要运行项目的同学可以使用手机号注册,将conf/user.ini配置文件的账号xxxx替换为自己注册的账号;<br> 
2.90duAuto目前公司的H5项目,功能/页面比较简单，主要采用python + selenium + unittest 搭建测试框架;<br> 
3.项目运行中test_suite文件执行已经载入的case，添加case时需要在test_suite引入对应的case模块,<br> 
  例如：from cases.detail_page_verify import DetailPageCase<br> 
        testcases = [DrawerMenuCase,DetailPageCase]<br> 
4.主要采用页面分离的形式设计,主要分为页面模块/公共方法模块/测试用了模块/测试报告等编写自动化测试脚本;<br> 
5.为了实现页面元素、页面功能、页面彻底的分类,目前将页面元素提取至pageElement目录下PageElement.xlsx中，页面的元素的变化直接更改Excel数据;<br> 
6.此项目仅提供给测试人员学习使用;<br> 
7.运行过程中如果有任何疑问添加QQ群：462635609<br> 
