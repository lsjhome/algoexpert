# 

class BST:
    
    def __init__(self, value):
        
        # value, left, right 지정
        pass
            
    # Average O(Log(n)) time | O(1) space (Iteration)
    # Worst case: O(n) time | O(1) space
    def insert(self, value):
        
        # 현재 노드를 지정하고
        # 원하는 위치가 나올때까지 계속 반복한다.
        
        # 현재 노드보다 값이 클때와 작을때를 분기해서 설정하고
        # 현재 노드보다 값이 작으면, 현재 노드를 현재 노드의 왼쪽으로 바꿔준다.
        # 다만 현재 노드의 왼쪽 노드에 값이 아무것도 없으면, 현재 노드의 왼쪽 값에 값을 넣어준다.
        
        # 현재 노드보다 값이 크면, 현재 노드를 현재 노드의 오른쪽으로 바꿔준다.
        # 다만 현재 노드의 오른쪽 노드에 값이 아무것도 없으면, 현재 노드의 오른쪽에 값을 넣어준다.        
        
        # self를 return
        # return self덕분에 testBst.insert(1).insert(5) 같은걸 할 수 있다.
        
        return self
    
    # Average: O(Log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        
        # 현재 노드를 지정하고
        # 현재 노드가 존재하지 않을 때까지 반복한다.
        # 만약 현재 노드의 값이 찾는 값보다 작으면, 현재 노드를 현재 노드의 왼쪽으로 바꾸고
        # 만약 현재 노드의 값이 찾는 값보다 크면, 현재 노드를 현재 노드의 오른쪽으로 바꾼다.
        # 만약 현재 노드의 값이 찾는 값이면, TRUE를 리턴한다.
        # 노드의 끝에 다달았는데도 값이 없으면 FALSE를 리턴한다.        

        return False
        
        
    def remove(self, value, parentNode = None):
        
        
        # 현재 노드의 값을 지정한다.
        # 현재 노드가 존재하지 않을 때까지 반복한다.
        
        # 만약 지우려는 값이 현재의 노드 값 보다 작다면
        # 부모 노드를 현재 노드로 변경하고
        # 현재 노드는 현재 노드의 왼쪽 노드로 교체한다.
        
        # 만약 지우려는 값이 현재의 노드 값보다 크다면
        # 부모 노드를 현재 노드로 변경하고
        # 현재 노드는 현재 노드의 오른쪽 노드로 교체한다.
        
        # 만약 값을 찾았으면
        # 현재 노드가 왼쪽노드 오른쪽 노드 양쪽이 다 있는 경우에는
        # 현재 노드의 오른쪽 노드의 가장 작은 값을 구하고, 이 값을 현재 노드의 값으로 교체한다.
        # 현재 노드의 오른쪽 노드에서 해당 값을 지워준다.
        
        # 만약 루트 노드이고 위에 해당하지 않는다면, 왼쪽 노드만 있거나, 오른쪽 노드만 있다는 것이다.
        # 왼쪽 노드만 있다면
        # 현재 노드의 값은 현재 노드의 왼쪽 노드의 값으로 변경하고
        # 현재 노드의 오른쪽은, 현재 노드의 왼쪽의 오른쪽으로
        # 현재 노드의 왼쪽은, 현재 노드의 왼쪽의 왼쪽으로
        # Overwrite 되지 않도록 순서에 유의한다.
        
        # 오른쪽 노드만 있다면,
        # 현재 노드의 값은, 현재 노드의 오른쪽 값으로 변경하고
        # 현재 노드의 왼쪽은, 현재 노드의 오른쪽 값의 왼쪽으로
        # 현재 노드의 오른쪽은, 현재 노드의 오른쪽 값의 오른쪽으로
        
        # 만약 루트 노드 하나가 있고, 자식노드가 둘다 없다면
        # 현재 노드의 값을 None으로 처리한다.
        
        # 위 경우들에 해당하지 않느다면, 왼쪽 혹은 오른쪽 둘중에 하나가 있거나 둘다 없다.

        # 만약 현재의 노드가 부모 노드의 왼쪽에 해당한다면, 즉 지금 보는 노드가 왼쪽 노드이면
        # 이제 부모 노드의 왼쪽 노드는 현재의 왼쪽 노드 혹은 오른쪽 노드로 바꾸어 준다.
        
        # 만약 현재의 노드가 부모 노드의 오른쪽에 해당한다면, 즉 지금 보는 노드가 오른쪽 노드이면
        # 이제 부모 노드의 오른쪽 노드는 현재의 왼쪽 노드 혹은 오른쪽 노드로 바꾸어 준다.
        
        # 위 해당 사항 중에 하나라도 걸리면 중지한다.
        
        return self
    
    
    def getMinValue(self):

        # 현재 노드를 지정한다.
        # 현재 노드의 왼쪽(작은 값)이 None이 될때까지 반복한다.
        # 현재 노드를 현재 노드의 왼쪽 노드들로 대채한다.
        # 반복이 끝난 후, 현재 노드의 값을 리턴한다.        
        pass
        
        
# 풀이
class BST:
    
    def __init__(self, value):
        
        # value, left, right 지정
        self.value = value
        self.left = None
        self.right = None
            
    # Average O(Log(n)) time | O(1) space (Iteration)
    # Worst case: O(n) time | O(1) space
    def insert(self, value):
        
        # 현재 노드를 지정하고
        # 원하는 위치가 나올때까지 계속 반복한다.
        
        # 현재 노드보다 값이 클때와 작을때를 분기해서 설정하고
        # 현재 노드보다 값이 작으면, 현재 노드를 현재 노드의 왼쪽으로 바꿔준다.
        # 다만 현재 노드의 왼쪽 노드에 값이 아무것도 없으면, 현재 노드의 왼쪽 값에 값을 넣어준다.
        
        # 현재 노드보다 값이 크면, 현재 노드를 현재 노드의 오른쪽으로 바꿔준다.
        # 다만 현재 노드의 오른쪽 노드에 값이 아무것도 없으면, 현재 노드의 오른쪽에 값을 넣어준다.        
        
        # self를 return
        # return self덕분에 testBst.insert(1).insert(5) 같은걸 할 수 있다.
        
        currentNode = self        
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left                
            else:                
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self
    
    # Average: O(Log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):

        # 현재 노드를 지정하고
        # 현재 노드가 존재하지 않을 때까지 반복한다.
        # 만약 현재 노드의 값이 찾는 값보다 작으면, 현재 노드를 현재 노드의 왼쪽으로 바꾸고
        # 만약 현재 노드의 값이 찾는 값보다 크면, 현재 노드를 현재 노드의 오른쪽으로 바꾼다.
        # 만약 현재 노드의 값이 찾는 값이면, TRUE를 리턴한다.
        # 노드의 끝에 다달았는데도 값이 없으면 FALSE를 리턴한다.        

        currentNode = self
        
        while currentNode is not None:
        
            if value < currentNode.value:
                currentNode = currentNode.left                
            
            elif value > currentNode.value:
                currentNode = currentNode.right                
            
            else:
                return True            

        return False        
    
    def remove(self, value, parentNode = None):

        # 현재 노드의 값을 지정한다.
        # 현재 노드가 존재하지 않을 때까지 반복한다.
        
        # 만약 지우려는 값이 현재의 노드 값 보다 작다면
        # 부모 노드를 현재 노드로 변경하고
        # 현재 노드는 현재 노드의 왼쪽 노드로 교체한다.
        
        # 만약 지우려는 값이 현재의 노드 값보다 크다면
        # 부모 노드를 현재 노드로 변경하고
        # 현재 노드는 현재 노드의 오른쪽 노드로 교체한다.
        
        # 만약 값을 찾았으면
        # 현재 노드가 왼쪽노드 오른쪽 노드 양쪽이 다 있는 경우에는
        # 현재 노드의 오른쪽 노드의 가장 작은 값을 구하고, 이 값을 현재 노드의 값으로 교체한다.
        # 현재 노드의 오른쪽 노드에서 해당 값을 지워준다.

        # 만약 루트 노드이고 위에 해당하지 않는다면, 왼쪽 노드만 있거나, 오른쪽 노드만 있다는 것이다.
        # 왼쪽 노드만 있다면
        # 현재 노드의 값은 현재 노드의 왼쪽 노드의 값으로 변경하고
        # 현재 노드의 오른쪽은, 현재 노드의 왼쪽의 오른쪽으로
        # 현재 노드의 왼쪽은, 현재 노드의 왼쪽의 왼쪽으로
        # Overwrite 되지 않도록 순서에 유의한다.
        
        # 오른쪽 노드만 있다면,
        # 현재 노드의 값은, 현재 노드의 오른쪽 값으로 변경하고
        # 현재 노드의 왼쪽은, 현재 노드의 오른쪽 값의 왼쪽으로
        # 현재 노드의 오른쪽은, 현재 노드의 오른쪽 값의 오른쪽으로
        # Overwrite 되지 않도록 순서에 유의한다.
        
        # 만약 루트 노드 하나가 있고, 자식노드가 둘다 없다면
        # 현재 노드의 값을 None으로 처리해서 값을 지워준다.

        # 위 경우들에 해당하지 않느다면, 왼쪽 혹은 오른쪽 둘중에 하나가 있거나 둘다 없다.

        # 만약 현재의 노드가 부모 노드의 왼쪽에 해당한다면, 즉 지금 보는 노드가 왼쪽 노드이면
        # 이제 부모 노드의 왼쪽 노드는 현재의 왼쪽 노드 혹은 오른쪽 노드로 바꾸어 준다.
        # 5 3 7 4
        
        # 만약 현재의 노드가 부모 노드의 오른쪽에 해당한다면, 즉 지금 보는 노드가 오른쪽 노드이면
        # 이제 부모 노드의 오른쪽 노드는 현재의 왼쪽 노드 혹은 오른쪽 노드로 바꾸어 준다.
        # 5 3 7 6
        
        # 위 해당 사항 중에 하나라도 걸리면 중지한다.        
        # Iteration을 탈출하고 self를 return해 준다.        
        
        currentNode = self
        
        while currentNode is not None:
        
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
                
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
                
            else:

                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                                    
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                        
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right                        
                    else:
                        currentNode.value = None
        
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right

                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                    
                break
                
        return self
    
    
    def getMinValue(self):
        
        # 현재 노드를 지정한다.
        # 현재 노드의 왼쪽 자식노드가 없을때 까지 반복한다.
        # 현재 노드를 현재 노드의 왼쪽 노드들로 대채한다.
        # 반복이 끝난 후, 현재 노드의 값을 리턴한다.
        
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left    
        return currentNode.value
