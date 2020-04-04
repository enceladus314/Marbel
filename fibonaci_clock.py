'''
Created on 01.01.2020

@author: jacBic
'''

if __name__ == '__main__':
    pass
else:
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Fibonacci clock")

        self.label = ttk.Label(self, text="Jacques")
        self.button_1 = ttk.Button(self, text="Fibonacci series",
                                   command=self.on_click_1)
        self.button_2 = ttk.Button(self, text="Clear",
                                   command=self.on_click_2)
        """
        #canvas1.1
        self.canvas_1_1 = Canvas(self,width=200, height=100)
        self.canvas_1_1.create_rectangle(50, 20, 150, 150, fill="#476042")
        #canvas1.2
        self.canvas_1_2 = Canvas(self,width=200, height=100)
        self.canvas_1_2.create_rectangle(50, 20, 150, 150, fill="#476042")
        #canvas2
        self.canvas_2 = Canvas(self,width=200, height=100)
        self.canvas_2.create_rectangle(50, 20, 150, 150, fill="#476042")
        #canvas3
        self.canvas_3 = Canvas(self,width=200, height=100)
        self.canvas_3.create_rectangle(50, 20, 150, 150, fill="#476042")
        #canvas5
        self.canvas_5 = Canvas(self,width=200, height=100)
        self.canvas_5.create_rectangle(50, 20, 150, 150, fill="#476042")
        """
        self.label.pack()
        
        size = 100 
        list_size_canvas = [size/4, size/4, size/2, size/2, size]
        list_size_canvas = [size/4, size/4, size/4, size/2, size]
        list_canvas = []
        
        anz_canvas = 5
        """
        for x in range(anz_canvas):
            self.loc_canvas = Canvas(self,width=200, height=100)
            list_canvas.append(self.loc_canvas)
            self.loc_canvas.create_rectangle(50, 20, 150, 150, fill="#476042")
            self.loc_canvas.pack()
        """
        
        self.button_1.pack()
        self.button_2.pack()
        #self.canvas_2.pack()
        #self.canvas_3.pack()
        
        self.fibonacci_list = [0,1]