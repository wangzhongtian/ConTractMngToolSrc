#-*- coding: UTF-8
from __future__ import print_function
import sys
全局记账方s= ("AAAA", "PPPP")  

状态类别=( "进行中","计划","完成",) 
    # 费用类别=("薪酬", "报销","管理费") 
合同大类=("增补合同", "增项","主合同")   
合同票别=("专票", "普票")  
合同税率=("3%","6%", "10%","11%", "13%" ,"16%","17%","0%")
def get合同税率( value ):
    rate2 =eval( str(value) )
    for htrate in 合同税率:
        htratestr=htrate.replace("%","*1.0/100*100").replace('"',"")
        rate1 = eval(htratestr);
        # print(value,htrate ,rate1,rate2)
        if abs( rate1- rate2 ) <= 0.01:
            return htrate
    htrate = "{:0.0f}%".format(rate2)
    return htrate
# 全局财务分类s=("销售合同",
#         "销售开票",
#         "销售收款",
#         "采购合同",
#         "采购收票",
#         "采购支出",
#         "费用合同",
#         "费用支出",
#         "报销收票","报销采购支出",
#         "直接采购支出","代赋税支出"
#         )     

全局费用子类s=("代付增值税","社保福利","薪酬","差旅费","合同管理费","招投标费","房租","转账手续费","临时用工","培训会议费","机动工程费","固定资产","临时材料采购","其它费用","主合同")
全局财务分类s=("销售合同",
        "销售开票",
        "销售收款",
        "采购合同",
        "采购收票",
        "采购支出",
        "费用合同",
        "费用支出",
        "报销收票","报销采购支出",
        "直接采购支出","代赋税支出"
        ) 
    
合同签署方式=("预估调整","变更程序","口头约定","正式合同") 
