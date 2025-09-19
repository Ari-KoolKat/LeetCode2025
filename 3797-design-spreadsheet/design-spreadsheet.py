class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.rows = rows
        self.cells = {}  

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.cells[cell] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
       
        parts = formula[1:].split('+')
        
        def get_operand_value(operand):
            
            if operand.isdigit():
                return int(operand)
            return self.cells.get(operand, 0)

        val1 = get_operand_value(parts[0])
        val2 = get_operand_value(parts[1])
        return val1 + val2