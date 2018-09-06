#!/usr/bin/env python3
# encoding=utf-8


# elasticsearch 6.4.0
# 也可以在elasticsearch界面下操作或者是在用postman工具
#


import requests

index_1 = 'http://localhost:9200/story/'
index_2 = 'http://localhost:9200/job/'
index_3 = 'http://localhost:9200/poll/'

index_story = {
            "settings":{
                "index":{
                    "number_of_shards":2,
                    "number_of_replicas":0
                }
            },
            "mappings":{
                "story":{
                    "_source":{
                        "enabled":"true"
                    },
                    "properties":{
                        "time":{
                            "type":"date"
                        },
                        "domain":{
                            "type":"text",
                            "index":"false"
                        },
                        "by":{
                            "type":"text",
                            "index":"false"
                        }
                    }
                }
            }
        }


index_job = {
            "settings":{
                "index":{
                    "number_of_shards":2,
                    "number_of_replicas":0
                }
            },
            "mappings":{
                "job":{
                    "_source":{
                        "enabled":"true"
                    },
                    "properties":{
                        "time":{
                            "type":"date"
                        },
                        "domain":{
                            "type":"text",
                            "index":"false"
                        },
                        "by":{
                            "type":"text",
                            "index":"false"
                        }
                    }
                }
            }
        }


index_poll = {
            "settings":{
                "index":{
                    "number_of_shards":2,
                    "number_of_replicas":0
                }
            },
            "mappings":{
                "poll":{
                    "_source":{
                        "enabled":"true"
                    },
                    "properties":{
                        "time":{
                            "type":"date"
                        },
                        "domain":{
                            "type":"text",
                            "index":"false"
                        },
                        "by":{
                            "type":"text",
                            "index":"false"
                        }
                    }
                }
            }
        }

index_lst = ([index_1, index_story], [index_2, index_job], [index_3, index_poll])

# 添加索引
for i, j in index_lst:
    requests.put(i, json=j)
