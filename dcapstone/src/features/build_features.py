data = pd.read_csv("online_store_customer_data.csv")
cd /Users/angeldurrani/Documents/GitHub/datacapstone/dcapstone/data/raw


gen_dumm = pd.get_dummies(data['Gender'])
gen_dumm["Female"] 
data = pd.concat([data,gen_dumm["Female"]],axis=1)
data = data.drop(["Gender"],axis=1)
data.rename(columns = {'Female':'Gender F=1,M=0'}, inplace = True)