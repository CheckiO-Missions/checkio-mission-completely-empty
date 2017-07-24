"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[]],
            "answer": True
        },{
            "input": [[[]]],
            "answer": True
        },{
            "input": [[[],[]]],
            "answer": True
        },{
            "input": [[1]],
            "answer": False
        },{
            "input": [[[],[1]]],
            "answer": False
        },{
            "input": [[0]],
            "answer": False
        },{
            "input": [['']],
            "answer": True
        },{
            "input": [[[],[{'':'No WAY'}]]],
            "answer": True
        },{
            "input": "[iter(())]",
            "answer": True
        },{
            "input": "[(),(),()]",
            "answer": True
        }

    ],
    "Extra": [
        {
            "input": [[[[[]]]]],
            "answer": True
        },{
            "input": [[[1],[1]]],
            "answer": False
        },{
            "input": [[None]],
            "answer": False
        },{
            "input": "[iter((1,))]",
            "answer": False
        },{
            "input": "[type('', (), {'__iter__': None})()]",
            "answer": False
        },{
            "input": "type('', (), {'__getitem__': ().__getitem__})()",
            "answer": False
        }
    ]
}
