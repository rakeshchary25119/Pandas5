import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    merge_df = pd.merge(employee, department, left_on = 'departmentId', right_on = 'id', how = 'left')
    merge_df = merge_df.rename(columns = {
        'id_x' : 'Employee_id',
        'name_x': 'Employee',
        'name_y': 'Department',
        'salary': 'Salary'
    })[['Department', 'Employee', 'Salary']]

    result = merge_df[merge_df['Salary'] == merge_df.groupby('Department')['Salary'].transform(max)]
    return result