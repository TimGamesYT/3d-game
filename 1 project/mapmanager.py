# напиши здесь код создания и управления картой
import pickle
class Mapmanager():
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        
        model = 'block'
        textures = [
            'block.png',
            'stone.png',
            'wood.png',
            'brick.png'
        ]
        self.createSamples(model, textures)
        self.colors = [
                      (0.2, 0.2, 0.35, 1),
                      (0.2, 0.5, 0.2, 1),
                      (0.7, 0.2, 0.2, 1),
                      (0.5, 0.3, 0.01, 1)]
        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode('Land')
    
    def createSamples(self, model, textures):
        self.samples = list()
        for t in textures:
            block = loader.loadModel(model)
            block.setTexture(loader.loadTexture(t))
            self.samples.append(block)
            
    
    def addBlock(self, position, b_type = 0):
        if b_type >= len(self.samples):
            b_type = 0
        block = self.samples[b_type].copyTo(self.land)
        block.setPos(position)
        if b_type == 0:
            self.color = self.getColor(int(position[2]))
            block.setColor(self.color)
        block.setTag('type', str(b_type))
        block.setTag('at', str(position))
        block.reparentTo(self.land)
        
    def delBlockFrom(self, position):
        x,y,z = self.findHighestEmpty(position)
        pos = x,y,z -1
        for block in self.find_block(pos):
            block.removeNode()
    def delBlock(self, position):
        blocks = self.find_block(position)
        for block in blocks:
            block.removeNode()
    
    def buildBlock(self, pos, b_type):
        x,y,z = pos
        new_pos = self.findHighestEmpty(pos)
        if new_pos[2] <= z+1:
            self.addBlock(new_pos, b_type)
            
    
    def find_block(self, position):
        return self.land.findAllMatches('=at=' + str(position))
    
    def isEmpty(self, pos):
        block = self.find_block(pos)
        if block:
            return False
        else:
            return True
        
    def findHighestEmpty(self, pos):
        x,y,z = pos
        z = 1
        while not self.isEmpty((x,y,z)):
            z+=1
        return (x,y,z)
    
    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[-1]
    def clear(self):
        self.land.removeNode()
        self.startNew()
        
    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(" ")
                for z in line:
                    for z0 in range(int(z) + 1):
                        block = self.addBlock((x, y, z0))
                    x+=1
                y+=1
        return x,y

    def saveMap(self):
        blocks = self.land.getChildren()
        with open('my_map.dat', 'wb') as fout:
            pickle.dump(len(blocks), fout)
            for block in blocks:
                x,y,z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, fout)
                pickle.dump(int(block.getTag("type")), fout)
    
    def loadMap(self):
        self.clear()
        with open("my_map.dat", 'rb') as fin:
            lenght = pickle.load(fin)
            for i in range(lenght):
                x,y,z = pickle.load(fin)
                b_type = pickle.load(fin)
                self.addBlock((x,y,z), b_type)