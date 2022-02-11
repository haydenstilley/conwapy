import comp

class Stage:
    
    bg = [[comp.Node(0,0) for _ in range(100)] for _ in range(100)]

    def drawNodes(self):
        for i in range(100):
            for j in range(100):
                self.bg[i][j].pos(i,j)

stage1 = Stage()
