from ast_nodes import (
    Program, Decl, Assign, Return, If, While, Block, Empty,
    BinOp, UnaryOp, Var, IntLit, FloatLit
)

def normalize(node):
    if isinstance(node,Var):
        node.name = "ID"

    if isinstance(node,IntLit):
        node.value = 0

    if isinstance(node,FloatLit):
        node.value = 0.0

    if isinstance(node,Assign):
        node.name = "ID"
        normalize(node.value)

    if isinstance(node,Program):
        for d in node.decls:
            normalize(d)
        for s in node.stmts:
            normalize(s)
        
    if isinstance(node,Decl):
        node.name = "ID"
        if(node.init):
            normalize(node.init)

    if isinstance(node,Return):
        if(node.value):
            normalize(node.value)
        
        
    if isinstance(node,If):
        normalize(node.cond)
        normalize(node.then_branch)
        if(node.else_branch):
            normalize(node.else_branch)

    if isinstance(node,While):
        normalize(node.cond)
        normalize(node.body)

    if isinstance(node,Block):
        for s in node.stmts :
            normalize(s)
    
    if isinstance(node,Empty):
        return
    
    if isinstance(node,BinOp):
        normalize(node.left)
        normalize(node.right)

    if isinstance(node,UnaryOp):
        normalize(node.operand)


def subtree_hash(node, hashs):
    if(node is None):
        return "None"
    
    elif isinstance(node,Var):
        h="Var(ID)"

    elif isinstance(node,IntLit):
        h="Int(0)"
    
    elif isinstance(node,FloatLit):
        h="Float(0.0)"

    elif isinstance(node,Assign):
        child_hash= subtree_hash(node.value , hashs)
        h =f"Assign(ID,{child_hash})"

    elif isinstance(node,Program):
        parts= []
        for d in node.decls:
            parts.append(subtree_hash(d,hashs))
        for s in node.stmts:
            parts.append(subtree_hash(s,hashs))
        h= f"Program({','.join(parts)})"
        
    elif isinstance(node,Decl):
        if(node.init):
            init_hash= subtree_hash(node.init,hashs)
        else:
            init_hash=""
        h=f"Decl(ID,{init_hash})"
        

    elif isinstance(node,Return):
        if(node.value):
            val_hash= subtree_hash(node.value,hashs)
        else:
            val_hash=""
        h=f"Return({val_hash})"
        
    elif isinstance(node,If):
        cond_hash=subtree_hash(node.cond,hashs)
        than_hash=subtree_hash(node.then_branch,hashs)
        if(node.else_branch):
            else_hash=subtree_hash(node.else_branch,hashs)
        
        else:
            else_hash=""

        h=f"If({cond_hash},{than_hash},{else_hash})"

    elif isinstance(node,While):
        condw_hash=subtree_hash(node.cond,hashs)
        body_hash=subtree_hash(node.body,hashs)
        h=f"While({condw_hash},{body_hash})"

    elif isinstance(node,Block):
        parts = [subtree_hash(s, hashs) for s in node.stmts]
        h=f"Block({','.join(parts)})"

    
    elif isinstance(node,BinOp):
        lhash=subtree_hash(node.left,hashs)
        rhash=subtree_hash(node.right,hashs)
        h=f"BinOp({node.op},{lhash},{rhash})"

    elif isinstance(node,UnaryOp):
        oprhash = subtree_hash(node.operand,hashs)
        h=f"UnaryOp({node.op},{oprhash})"

    else:
        h="Unknown"

    hashs.append(h)
    return h

def find_subs(ast_root):
    hashs = []
    subtree_hash(ast_root,hashs)
    return hashs


def sub_matching(ast_a , ast_b):
    normalize(ast_a)
    normalize(ast_b)


    hash_list_a = find_subs(ast_a)
    hash_list_b = find_subs(ast_b)

    setA=set(hash_list_a)
    setB=set(hash_list_b)

    intersection = setA & setB
    union = setA | setB

    if len(union) ==0:
        return 0
    
    result = {
        "ast_similarity": round(len(intersection)/len(union),1)
    }
    
    return result
