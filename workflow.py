import molflow.definitions as defs

workflow = defs.WorkflowDefinition('add_two_to_it')
__workflow__ = workflow

# Inputs
number = workflow.add_input('number', description='Number to add two to', type='number')

# Functions
add_one = defs.Function('add_one', sourcefile='./functions.py')

# Workflow
p1 = add_one(number)
p2 = add_one(p1)

# Outputs
workflow.set_output(p2, 'result', description='Original number plus two', type='number')