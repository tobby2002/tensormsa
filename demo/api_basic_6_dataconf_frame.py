import requests
import json, os

url = "{0}:{1}".format(os.environ['HOSTNAME'] , "8000")



resp = requests.post('http://' + url + '/api/v1/type/wf/state/dataconf/detail/frame/nnid/nn00004/ver/2/node/dataconf_node/',
                     json={"label":
                               {"income_bracket": "LABEL"}
                         , "Transformations":
                               {"col1": {"boundaries": [18, 25, 30, 35, 40, 45, 50, 55, 60, 65], "column_name": "age"}}
                         , "cross_cell": {"col12": {"column2_0": "native_country", "column2_1": "occupation"}
                             , "col1": {"column_1": "occupation", "column_0": "education"}}
                         , "cell_feature":
                               {"hours_per_week": {"column_type": "CONTINUOUS"}
                                   , "capital_loss": {"column_type": "CONTINUOUS"}
                                   , "age": {"column_type": "CONTINUOUS"}
                                   , "capital_gain": {"column_type": "CONTINUOUS"}
                                   , "education_num": {"column_type": "CONTINUOUS"}
                                   , "education": {"column_type": "CATEGORICAL"}
                                   , "occupation": {"column_type": "CATEGORICAL"}
                                   , "workclass": {"column_type": "CATEGORICAL"}
                                   , "gender": {"keys": ["female", "male"]
                                   , "column_type": "CATEGORICAL_KEY"}
                                   , "native_country": {"column_type": "CATEGORICAL"}
                                   , "relationship": {"column_type": "CATEGORICAL"}
                                   , "marital_status": {"column_type": "CATEGORICAL"}
                                   , "race": {"column_type": "CATEGORICAL"}

                                }
                           })
data = json.loads(resp.json())
print("evaluation result : {0}".format(data))