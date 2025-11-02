import os
from browserforge.headers import HeaderGenerator

headerGenerator = HeaderGenerator()
PREV_DATE = "20250929"
CURR_DATE = "20251029"
PROJECT_NAME = "audiobee_uhc_individual"

REQ_STATE_CODES = [
    "AL",
    "AZ",
    "CO",
    "FL",
    "GA",
    "IL",
    
    "KS",
    "LA",
    "MD",
    "MA",
    "MI",
    "MS",
    
    "MO",
    "NJ",
    "NM",
    "NY",
    "NC",
    "OH",
    
    "OK",
    "SC",
    "TN",
    "TX",
    "VA",
    
    "WA",
    "WI",
    "IA",
    "IN",
    "NE",
    "WY"
]
DIRS = {
    "raw": os.path.join(CURR_DATE, "raw"),
    "search_results": os.path.join(
        CURR_DATE,
        "raw",
        "search_results",
    ),
    "provider_details": os.path.join(
        CURR_DATE,
        "raw",
        "provider_details",
    ),
    "raw_processed": os.path.join(CURR_DATE, "raw", "processed"),
    "output": os.path.join("output"),
    "plan_output": os.path.join("output", "plans"),
    "processed": os.path.join(CURR_DATE, "processed"),
}
PREV_DIRS = {
    "raw": os.path.join(PREV_DATE, "raw"),
    "search_results": os.path.join(
        PREV_DATE,
        "raw",
        "search_results",
    ),
    "provider_details": os.path.join(
        PREV_DATE,
        "raw",
        "provider_details",
    ),
    "raw_processed": os.path.join(PREV_DATE, "raw", "processed"),
    "output": os.path.join("output"),
    "plan_output": os.path.join("output", "plans"),
    "processed": os.path.join(PREV_DATE, "processed"),
}
POINTS = {
    "AL": {
        "radius": 100,
        "points": [
            [-87.75670539713039, 31.182324055517807],
            [-87.25813067420617, 33.131893454452246],
            [-87.25813067420617, 34.585068776513424],
            [-85.80495535214497, 31.678718132391047],
            [-85.80495535214497, 33.131893454452246],
            [-85.80495535214497, 34.585068776513424],
        ],
        "plans": {
            "AL Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IkFMIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTE0IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYy5leGNoYW5nZSIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMDEifQjcHe67dph6-bNVjWEMLuXhZvCDKsM8p-9Qc0LtHWWl4&planYear=2026",
        },
    },
    "AZ": {
        "radius": 100,
        "points": [
            [-114.0387078200294, 32.97210961657392],
            [-113.12267955391337, 34.36986162337591],
            [-113.86592088968035, 35.922803998764394],
            [-111.84412275821668, 32.71775954849966],
            [-111.71284292843802, 36.20529890286488],
            [-111.24759651620806, 35.438380248117255],
            [-110.06237059020779, 32.19682481683884],
            [-110.0090078460398, 34.258749068507115],
            [-109.59692986729007, 36.20218966405871],
        ],
        "plans": {
            "AZ Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IkFaIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTA3IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYy5leGNoYW5nZSIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMDQifQYvUU9nANb1lUPoE0BFnxMwhYShd9SUI8BvjV4gj91Xo&planYear=2026",
        },
    },
    "CO": {
        "radius": 100,
        "points": [
            [-108.1601060869408, 38.0794597590134],
            [-108.40629351760916, 40.389600770441184],
            [-106.94198518964083, 37.93730063118112],
            [-106.65264393732747, 40.23944700046928],
            [-105.0517696051043, 38.00709604034957],
            [-104.73040998380952, 40.24106761971149],
            [-103.05063151183973, 38.009140129363075],
            [-103.00420696129518, 40.034300543405024],
        ],
        "plans": {
            "RMHP Colorado Doctors Plan / RMHP Colorado Doctors Plan CO Option": "eyJwbGFuTmFtZSI6IlJNSFAgQ29sb3JhZG8gRG9jdG9ycyBQbGFuIC8gUk1IUCBDb2xvcmFkbyBEb2N0b3JzIFBsYW4gQ08gT3B0aW9uIiwiZGVsc3lzIjoiOTE4IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYy5leGNoYW5nZSIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMDgifQCBzUEPeAVAi6KE2zHrQJvPwkhrW5mZqgXkiPFOvrT3E&planYear=2026",
            "RMHP Monument Health": "eyJwbGFuTmFtZSI6IlJNSFAgTW9udW1lbnQgSGVhbHRoIiwiZGVsc3lzIjoiOTE1IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYy5leGNoYW5nZSIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMDgifQnKMUQUN8fti0ZdiIiLuAPa06WKBQr67B33YpXO7BcnY&planYear=2026",
            "RMHP Monument ONE / RMHP Monument ONE CO Option": "eyJwbGFuTmFtZSI6IlJNSFAgTW9udW1lbnQgT05FIC8gUk1IUCBNb251bWVudCBPTkUgQ08gT3B0aW9uIiwiZGVsc3lzIjoiOTE2IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYy5leGNoYW5nZSIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMDgifQ9t0h8-c_MvQezDnQ5W7FvLv1O6jEYwQKTGKZHR6znyw&planYear=2026",
            # Deleted # "RMHP Sky / RMHP Sky CO Option": "eyJwbGFuTmFtZSI6IlJNSFAgU2t5L1JNSFAgU2t5IENPIE9wdGlvbiIsImRlbHN5cyI6IjkyNiIsImNvdmVyYWdlVHlwZSI6Im1lZGljYWwiLCJwYXJ0bmVySWQiOiJ1aGMuZXhjaGFuZ2UiLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMDgifQD0JmjDL_L6k2aq3X3icNypq8QBQbEb6pCog1NzQTUUU",
            "RMHP Valley / RMHP Valley CO Option": "eyJwbGFuTmFtZSI6IlJNSFAgVmFsbGV5IC8gUk1IUCBWYWxsZXkgQ08gT3B0aW9uIiwiZGVsc3lzIjoiOTE3IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYy5leGNoYW5nZSIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMDgifQnRHrkFrUOTAlVseGuw5gQyridyr6Qcib1ZpGxISJ4XY&planYear=2026",
        },
    },
    "FL": {
        "radius": 100,
        "points": [
            [-84.33867723697375, 30.00118092061065],
            [-86.73197110253804, 30.77164119863744],
            [-82.76124796096542, 27.139650704662557],
            [-81.64682567671417, 29.059497144153497],
            [-82.3699970552698, 30.107600600523206],
            [-81.00876346357597, 25.322064862946313],
            [-81.22731360271703, 27.116343410689176],
        ],
        "plans": {
            "FL Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IkZMIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTEwIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMTIifQtNKx7sGcDcyr8LJuHylvgD775n7voTmFg39S-FOgiZA&planYear=2026",
        },
    },
    "GA": {
        "radius": 100,
        "points": [
            [-84.19609405601803, 31.57031910952132],
            [-84.83296371143636, 33.54061769453301],
            [-84.34455875320461, 34.604473581887355],
            [-82.86853115321995, 31.70974602782747],
            [-82.83598583689877, 33.54061769453301],
            [-81.68188623697634, 31.578919935292397],
        ],
        "plans": {
            "GA Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IkdBIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTEyIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMTMifQVBa_nYkYRE_XvVk2f35tLsdtJnrlbCcgg8HHizD5QBY&planYear=2026",
        },
    },
    "IL": {
        "radius": 100,
        "points": [
            [-89.63910938375139, 38.604352642848596],
            [-90.98553494238307, 39.971959793104986],
            [-90.16177183718847, 41.429190878239446],
            [-88.82464709830305, 38.09282149609777],
            [-88.26868635146171, 39.83432553228471],
            [-87.97244090899513, 42.109759002020326],
        ],
        "plans": {
            "IL Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IklMIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTEzIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMTcifQukvAJhwwAG81Av8DfsNnJJKIHPIjh-qKtoYQBMXK3GI&planYear=2026",
        },
    },
    "KS": {
        "radius": 100,
        "points": [
            [-101.16011446505973, 38.03746272876662],
            [-101.83116489436168, 39.874682304372826],
            [-95.2060268828586, 38.07772472393084],
            [-100.24558402756817, 40.36067084682588],
            [-99.2025180900939, 38.00200391508599],
            [-98.49373542183721, 40.36383017549495],
            [-97.07271934545906, 37.94568477699032],
            [-97.08371768538271, 39.937717490086925],
            [-96.05245417979798, 39.16589989513008],
        ],
        "plans": {
            "KS Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IktTIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTIwIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMjAifQfrcyvevKBZk4usKJhlbGGLShFcRso47gizNb8GDXPG8&planYear=2026",
        },
    },
    "LA": {
        "radius": 100,
        "points": [
            [-92.95636121494566, 30.2301610952106],
            [-92.95636121494566, 31.93086376966712],
            [-92.95636121494566, 32.844970877819286],
            [-91.64895632364131, 30.230161095210605],
            [-91.64895632364131, 32.844970877819286],
            [-90.03642278369567, 29.790335420663496],
        ],
        "plans": {
            "LA Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IkxBIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTA5IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMjIifQh0NG9bHR7y3l0ACOBYAjCvb1cyMzZPiz9oA4Hz2_frg&planYear=2026",
        },
    },
    "MA": {
        "radius": 100,
        "points": [
            [-73.1794329916643, 42.82231865106847],
            [-70.72816906443015, 42.148555736621994],
        ],
        "plans": {
            "Navigate EPO": "eyJwbGFuTmFtZSI6Ik5hdmlnYXRlIEVQTyIsImRlbHN5cyI6Ijk0NSIsImNvdmVyYWdlVHlwZSI6Im1lZGljYWwiLCJwYXJ0bmVySWQiOiJ1aGMiLCJsYW5ndWFnZSI6ImVuIiwic2hvd0Nvc3RzIjp0cnVlLCJmaXBzQ29kZSI6IjI1In0CCybyPQNxz2taUGu2JOA5cDpTOtMdVAY60b9OiZRI6E&planYear=2026",
        },
    },
    "MD": {
        "radius": 100,
        "points": [
            [-78.33771725171414, 39.40868574508479],
            [-76.3952593335658, 38.69784265467148],
        ],
        "plans": {
            "MD Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6Ik1EIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTA1IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMjQifQ60GVcE6RW6ml8HmSZQKJzUZReQkhQg8ut9NIn9zy7oo&planYear=2026",
        },
    },
    "MI": {
        "radius": 100,
        "points": [
            [-89.59904400874235, 46.80284701115008],
            [-88.65579495143199, 48.12360195751201],
            [-87.62542613080292, 46.70051162543409],
            [-86.09540248235345, 42.66882320183846],
            [-86.41861281004596, 44.62648689244085],
            [-85.91229939960738, 46.73671898770746],
            [-84.29164003531397, 42.82279979729166],
            [-84.55582830562915, 45.19262341980706],
            [-82.6996396456116, 43.12705104886652],
            [-82.75811978322685, 44.97017657042689],
        ],
        "plans": {
            "MI Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6Ik1JIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTExIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMjYifQe2KmrF5urh3XHwvgbI4wS82vnoZvi5qY3qseNMn_k9U&planYear=2026",
        },
    },
    "MS": {
        "radius": 100,
        "points": [
            [-90.56112520238504, 31.740961822493986],
            [-90.80968452440989, 33.40324732559564],
            [-89.96919033174474, 35.11488583852413],
            [-88.86014894840064, 31.3725887902373],
            [-89.42246471633761, 32.84070451218006],
            [-88.14725487271299, 35.06234047995427],
        ],
        "plans": {
            "MS Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6Ik1TIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTIyIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMjgifQ714rMjDZek4dziZY1r5mO8tKaPOf_qFRjKmYWca85DE&planYear=2026",
        },
    },
    "MO": {
        "radius": 100,
        "points": [
            [-93.59254639625917, 37.40063422509372],
            [-93.53264716153248, 39.98275784196551],
            [-92.06444542774528, 37.696570455072276],
            [-91.19939246120072, 39.678855825343334],
            [-90.29503089371116, 37.3137489155599],
            [-95.23869814215102, 39.69493429980241],
        ],
        "plans": {
            "MO Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6Ik1PIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTIxIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMjkifQE4vcAEaHRk9MqseVqobV2jbBlwlQMBpMGTTiYPKPzjE&planYear=2026",
        },
    },
    "NJ": {
        "radius": 100,
        "points": [[-74.71142300365858, 40.03065199785475]],
        "plans": {
            "New Jersey Oxford Metro Network": "eyJwbGFuTmFtZSI6Ik5ldyBKZXJzZXkgT3hmb3JkIE1ldHJvIE5ldHdvcmsiLCJkZWxzeXMiOiI5MjgiLCJjb3ZlcmFnZVR5cGUiOiJtZWRpY2FsIiwicGFydG5lcklkIjoidWhjIiwibGFuZ3VhZ2UiOiJlbiIsInNob3dDb3N0cyI6dHJ1ZSwiZmlwc0NvZGUiOiIzNCJ9mkxDdple7e1aKlW4Zjh6COx_ibGatEjDihVqKXHqea4&planYear=2026",
        },
    },
    "NM": {
        "radius": 100,
        "points": [
            [-107.90836425031651, 32.22277122138851],
            [-106.9150635308215, 34.833987641915314],
            [-108.19950567872846, 37.16959549979839],
            [-105.6239628099325, 33.16978749679478],
            [-104.76640820036114, 35.728743769594445],
            [-105.70439650278905, 36.7163200017128],
            [-103.92137155801908, 33.167017546709914],
            [-108.89571349929139, 34.55480341315739],
            [-103.5695815493133, 35.66741975317662],
        ],
        "plans": {
            "New Mexico Choice Network": "eyJwbGFuTmFtZSI6Ik5ldyBNZXhpY28gQ2hvaWNlIE5ldHdvcmsiLCJkZWxzeXMiOiI5MjUiLCJjb3ZlcmFnZVR5cGUiOiJtZWRpY2FsIiwicGFydG5lcklkIjoidWhjIiwibGFuZ3VhZ2UiOiJlbiIsInNob3dDb3N0cyI6dHJ1ZSwiZmlwc0NvZGUiOiIzNSJ9wH9bCyeKX1UwodW_Pb3TyA1TqIHVeu_h_9OZoaxydng&planYear=2026",
        },
    },
    "NY": {
        "radius": 100,
        "points": [
            [-78.38978557825428, 42.25389008102712],
            [-75.62709996780703, 42.318553252985566],
            [-73.17181950047859, 41.44415403556073],
            [-74.28644055055295, 43.91971890980669],
            [-76.79492092739264, 44.11996399941259],
        ],
        "plans": {
            "Compass HMO NY State of Health Marketplace": "eyJwbGFuTmFtZSI6IkNvbXBhc3MgSE1PIE5ZIFN0YXRlIG9mIEhlYWx0aCBNYXJrZXRwbGFjZSIsImRlbHN5cyI6Ijk0NCIsImNvdmVyYWdlVHlwZSI6Im1lZGljYWwiLCJwYXJ0bmVySWQiOiJ1aGMiLCJsYW5ndWFnZSI6ImVuIiwic2hvd0Nvc3RzIjp0cnVlLCJmaXBzQ29kZSI6IjM2In0FNgGCHqRpW5bviWfUzleRuMVMCkDFu4ODQmftLuZ81U&planYear=2026",
        },
    },
    "NC": {
        "radius": 100,
        "points": [
            [-83.3832555857863, 35.22422065240747],
            [-81.90956007817692, 35.73375924055894],
            [-79.84106001030082, 35.669903937147424],
            [-78.37407437318444, 35.13021108139617],
            [-77.15661890883737, 35.78455509066505],
            [-75.79019280534283, 35.150461477567674],
        ],
        "plans": {
            "NC Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6Ik5DIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTAxIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMzcifQ6SYzrH80LrSHi9j5AjbZZC0r4R44YXJ_778FxuMjZz8&planYear=2026",
        },
    },
    "OH": {
        "radius": 100,
        "points": [
            [-83.67485654041187, 39.834546449944085],
            [-83.78329480357587, 41.659443015768076],
            [-82.00419344707716, 39.6772515409779],
            [-81.27052461542944, 41.40311158900593],
        ],
        "plans": {
            "OH Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6Ik9IIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTIzIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMzkifQJwfO-33sSz1TKOaoTqxtZ6rKtdMGvRKmsqgzniDqxUo&planYear=2026",
        },
    },
    "OK": {
        "radius": 100,
        "points": [
            [-102.82907548505312, 36.50865510157615],
            [-100.24783741150935, 36.68393473459915],
            [-99.25911533777423, 35.409251734206975],
            [-99.21742982145341, 36.757080314166785],
            [-97.31468340795948, 34.85459528442453],
            [-97.07914151112061, 36.787677157907495],
            [-95.3433122456857, 34.69434109483771],
            [-95.48299669960039, 36.38844979840809],
        ],
        "plans": {
            "OK Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6Ik9LIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTAyIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiNDAifQ3IwjystfmgaLeg6ng1-I01Kf1e0LmBBjhqb1zxPtvxY&planYear=2026",
        },
    },
    "SC": {
        "radius": 100,
        "points": [
            [-82.1850689298821, 34.18836988314415],
            [-81.69465432668453, 34.93875677185888],
            [-80.11423940189673, 33.37238266474275],
        ],
        "plans": {
            "SC Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IlNDIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTI0IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiNDUifQh8Yv9zuhzPIA3MuJtMYXsft7bRG87gi3a-dUSZdYboM&planYear=2026",
        },
    },
    "TN": {
        "radius": 100,
        "points": [
            [-89.83444793278153, 36.17474877677465],
            [-88.57797128261164, 36.25483178298485],
            [-86.86993757957359, 35.704689917007585],
            [-84.97167090516331, 35.98249988374201],
            [-83.05452331812516, 36.61896244172289],
        ],
        "plans": {
            "TN Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IlROIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTA2IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiNDcifQg1XOLt8g-wtDeng9wELq1aIFYbVgi3kb5A4tkW6LzXk&planYear=2026",
        },
    },
    "TX": {
        "radius": 100,
        "points": [
            [-105.44047731047554, 31.337774253045026],
            [-103.59009588405912, 29.730055628969765],
            [-103.37851418896986, 31.33895173089995],
            [-102.55173692455477, 33.46553397335301],
            [-102.50811345010464, 35.73881491113326],
            [-101.42667695753555, 30.93738331941288],
            [-100.98659927643678, 33.066563616850374],
            [-100.93084463599666, 35.51700101460381],
            [-99.21184892389029, 27.482843733482675],
            [-100.19858445212054, 29.443931690281794],
            [-99.69019744425077, 31.186832275954117],
            [-99.36618863266781, 33.20148841016854],
            [-97.57246946609376, 27.220164233505372],
            [-97.67484957101462, 29.33409001584531],
            [-97.87788935707991, 31.365839779128457],
            [-97.26291002082067, 33.31109891235688],
            [-95.61460141200615, 29.32521388377176],
            [-96.37794788666744, 31.28060471987645],
            [-95.12281509172546, 33.15828327297433],
            [-94.02894845811923, 30.96474767783196],
        ],
        "plans": {
            "TX Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IlRYIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTA4IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiNDgifQMQFY_1U6GK3dWzJO0xysxZD0H-Ei_AJ0Wm_n0zlgcUI&planYear=2026",
            "TX Kelsey-Seybold Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IlRYIEtlbHNleS1TZXlib2xkIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTMzIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiNDgifQXmvT5Dh8azZlM00ptmfLp0BrlP0yAn-7TQUdErUzIbs&planYear=2026",
            "TX Sanitas Anchor Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IlRYIFNhbml0YXMgQW5jaG9yIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCIsImRlbHN5cyI6Ijk0NiIsImNvdmVyYWdlVHlwZSI6Im1lZGljYWwiLCJwYXJ0bmVySWQiOiJ1aGMuZXhjaGFuZ2UiLCJsYW5ndWFnZSI6ImVuIiwic2hvd0Nvc3RzIjp0cnVlLCJmaXBzQ29kZSI6IjQ4In0B_6Q323L9wHzkAf22cjU43lZYKLoyfNzTYw8nrMBL04&planYear=2026",
        },
    },
    "VA": {
        "radius": 100,
        "points": [
            [-80.73808583911057, 37.57369310251927],
            [-78.88360232938184, 37.39117647925215],
            [-82.77586947234298, 37.591876595222374],
            [-77.84607418952024, 38.78772843113995],
            [-77.61409458466323, 37.37064982009295],
            [-75.86922576449086, 37.8045087075204],
        ],
        "plans": {
            "VA Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IlZBIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTA0IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiNTEifQIwwL61d_w-TXvGLLRmXtTHjRFYMEmhpC8N2dhVvN3wI&planYear=2026",
        },
    },
    "WA": {
        "radius": 100,
        "points": [
            [-123.49384044779461, 46.87948371805836],
            [-121.80167900289322, 46.45765404998329],
            [-123.77976695380079, 48.563231643573424],
            [-120.43935132763218, 47.1103320550155],
            [-120.26973031325878, 48.56323164357344],
            [-119.34958748574277, 47.11033205501551],
            [-122.32588429951092, 48.56323164357344],
            [-117.5063253611338, 47.1103320550155],
            [-117.89668789718493, 48.56323164357344],
        ],
        "plans": {
            "WA Charter EPO": "eyJwbGFuTmFtZSI6IldBIENoYXJ0ZXIgRVBPIiwiZGVsc3lzIjoiOTAzIiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiNTMifQCmlzAheqDm3HEvws4B7bgKIKMx8sKySTaF158inF8sE&planYear=2026",
        },
    },
    "WI": {
        "radius": 100,
        "points": [
            [-90.11949501801928, 43.56651530373634],
            [-92.26608789641386, 45.23651721755249],
            [-88.07597955327137, 43.47435445555925],
            [-90.94653829133125, 46.24035349805617],
            [-87.21893741834094, 44.247567820081954],
            [-89.21500198256024, 45.734701269769275],
        ],
        "plans": {
            "WI Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IldJIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTI5IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiNTUifQthL92I-Zq3DdkTpp3rSdOPMyFkEic02pHhpmQe_TX7Y&planYear=2026",
        },
    },
    "IA": {
        "radius": 100,
        "points": [
            [-94.74604293383945, 41.496236295063206],
    [-91.32311508710875, 42.289994689738045],
    [-95.67974219906075, 42.5429804690748],
    [-92.37330023720877, 41.44349287482506],
    [-93.4063543349453, 42.744555183597456]
        ],
        "plans": {
            "IA Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IklBIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTM1IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMTkifQZeh3JCcC1Cwy4w4G88NiWX_YP-At1teviP3p_UiNO9U&planYear=2026",
        },
    },
    "IN": {
        "radius": 100,
        "points": [
    [-85.9104266689311, 39.345101880378756],
    [-87.68696250824578, 38.678609153656566],
    [-87.65953171735063, 41.018795361780526],
    [-85.4389409242178, 41.49085176221466]
        ],
        "plans": {
            "IN Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6IklOIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTM0IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMTgifQDeOYzlG5JmlgkSmDaXa4SSZIQTp05njUA-Huy6higNU&planYear=2026",
        },
    },
    "NE": {
        "radius": 100,
        "points": [
    [-96.18808169598393, 41.16819000811071],
    [-98.3785082899257, 40.46867763936073],
    [-98.23048747692032, 42.28302287189944],
    [-100.72161058018567, 42.0979504856003],
    [-103.0475806736376, 41.961758798486684],
    [-100.94220142303357, 40.414018906474794]
        ],
        "plans": {
            "NE Individual Exchange Benefit Plan": "eyJwbGFuTmFtZSI6Ik5FIEluZGl2aWR1YWwgRXhjaGFuZ2UgQmVuZWZpdCBQbGFuIiwiZGVsc3lzIjoiOTM2IiwiY292ZXJhZ2VUeXBlIjoibWVkaWNhbCIsInBhcnRuZXJJZCI6InVoYyIsImxhbmd1YWdlIjoiZW4iLCJzaG93Q29zdHMiOnRydWUsImZpcHNDb2RlIjoiMzEifQtm6vjysuH1BVzMSiGx9ze7yQJO8kG0pNmS1WU8Fi1Cw&planYear=2026",
        },
    },
    "WY": {
        "radius": 100,
        "points": [
    [-105.11527655422215, 41.790469578107185],
    [-106.89173672622938, 43.9058454656653],
    [-107.61382115924651, 41.640016827308756],
    [-108.74789572723195, 43.87241620092746],
    [-110.17040050516842, 43.98811442223722],
    [-109.98304852497023, 41.97449314900677],
    [-105.06196459753801, 43.984053773727375]
        ],
        "plans": {
            "Wyoming Choice Network": "eyJwbGFuTmFtZSI6Ild5b21pbmcgQ2hvaWNlIE5ldHdvcmsiLCJkZWxzeXMiOiI5MzciLCJjb3ZlcmFnZVR5cGUiOiJtZWRpY2FsIiwicGFydG5lcklkIjoidWhjIiwibGFuZ3VhZ2UiOiJlbiIsInNob3dDb3N0cyI6dHJ1ZSwiZmlwc0NvZGUiOiI1NiJ9958M0R5VeO2U0eF33rzFeVx27jchsH4hQf2iAAh70qY&planYear=2026",
        },
    }
}

BASE_SEARCH_URL = "https://connect.werally.com/rest/provider/v4/search/filtered"
BASE_PROVIDER_DETAILS_URL = "https://connect.werally.com/rest/provider/v3/partners/{plan_configuration}/providerTypes/{provider_type}/providers/{provider_id}"
# LOGIN_URL = (
#     "https://connect.werally.com/rest/user/v1/guest/login?token={token}&planYear=2025"
# )
LOGIN_URL = (
    "https://connect.werally.com/rest/user/v1/guest/login?token={token}"
)
PLAN_URL = "https://connect.werally.com/rest/partner/v1/partners/uhc/plan?coverageType=medical&planCode={plan_code}"
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en",
    "context-config-consumersource": "connect-web",
    "context-config-partnergroup": "uhc",
    "context-config-partnerid": "uhc.exchange",
    # "context-config-plancode": "COCHIP",
    "context-provider-routing": "uhc",
    "current-connect-session-type": "guest",
    "priority": "u=1, i",
    "referer": "https://connect.werally.com/search/providers/80040/page-1?coverageType=medical&hasHcbsServices=false&lat=39.741095&long=-104.875075&role=1&sort=uhpd&specialtyCategory=56",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "context-config-plancode": "914",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}
HEADERS_PROVIDER_DETAILS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en",
    "content-type": "application/json",
    "context-config-consumersource": "connect-web",
    "context-config-partnerid": "uhc.exchange",
    "context-provider-routing": "uhc",
    "context-config-plancode": "914",
}
HEADERS_NEW = {
    "Accept-Language": "en",
    "Context-Config-ConsumerSource": "connect-web",
    "Context-Config-PartnerId": "uhc.medicaid",
    "Context-Config-PartnerGroup": "uhc",
    "Context-Config-PlanCode": "FLCAID",
    "Context-Provider-Routing": "uhc",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://connect.werally.com/search/providers/80045/page-1",
}


def get_headers_ua_random():
    return headerGenerator.generate()


PARAMS = {
    # "center": "-112.134291,33.553104",
    "configuration": "uhc.exchange",
    "from": "0",
    # "role": ["1", "12", "13"],
    # "searchType": ["place", "medicalGroup", "person"],
    "selectedLang": "en",
    "sort": "nameAZ",
    "networks.medical": [],
}