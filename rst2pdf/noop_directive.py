from docutils.parsers import rst

def noop_directive(name, arguments, options, content, lineno,
                 content_offset, block_text, state, state_machine):
    node_list = []
    return node_list
    
noop_directive.content = ["*"]
