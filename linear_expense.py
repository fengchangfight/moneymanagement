# -*- coding:utf-8 -*-
import pandas as pd
from datetime import date

expense_log = "/Users/xiefengchang/life/linear_expense.xlsx"
daily_expense_limit = 70

if __name__ == "__main__":
    print("基准日开支值为:{0}".format(daily_expense_limit))
    today = date.today()
    excel_data_df = pd.read_excel(expense_log, sheet_name='Sheet1')
    df = pd.DataFrame(excel_data_df, columns=[
                      '开支名', '开支', '起始日期', '效用日', '到期日期'])
    for index, row in df.iterrows():
        due_date = row['到期日期']
        if(today > due_date):
            continue
        averageExpense = row['开支']/row['效用日']
        daily_expense_limit = daily_expense_limit - averageExpense
        print("扣除开支{0}({1})的{2}日分摊开支{3}元...".format(
            row['开支名'], row['开支'], row['效用日'], averageExpense))
    print('今日可用开支额度为:{0}元'.format(daily_expense_limit))
