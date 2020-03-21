# 合同管理工具 ContractManager
keywords：集成项目合同管理工具、 Ironpython 、winform GUI 、Windows(.Net Framework)、 Linux(mono) 、powershell 、pickle内存数据库、自定义py1文件格式的内存数据库。

functions:
 销售合同、采购合同管理： 新建、修改、查看
 销售收款、采购支付管理： 新建、修改、查看
 销售发票、采购发票管理： 新增、修改、查看
 费用类：员工报销、薪酬、福利： 新增、修改、查看
 其它类： 管理费、代缴税等：同上。
 按照记账方、对方、项目分类、财务分类、起止时间搜索响应的项目合同信息，并列表显示、核算对应的30多个财务统计数据，并显示在表格中。
 将对应记账方的所有的合同信息分类显示并导出到excel格式的文件中。
 可方便地提取和合并不同人员记录的合同数据；
 采用上下文菜单将列表显示的合同信息、财务统计数据导出到剪贴板中，方便拷贝到Excel文件、或者其它类型的文档中。
 
Enviroment：
 windows: .Net Framework
 Ubuntu Linux:mono runtime(need modify some mono source code to show correct Chinese characters),GDIPlus
 Ironpython: 2.7.7
 if needed,Can be compiled into binary format Exe(windows or Linux)
 
Folder：
ipycode ： ironpython code file
xlsProLib： Write data to xml file which can be opened by Excel
01-psIPY:  entry to the tools.
     z04前期后期账务处理.ps1 : Example powershell script code to show how to execute the ironpython script
     glbcfg-前期后期账务.py: configure python file ,which will be copy to .. folder in the running stage.

other information：
 A00-xxx、A02-xxx、C001-xxx、C01-xxx、T00-xxx文件为相关的数据转换脚本文件。
