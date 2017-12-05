
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._ayudaToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._salirToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._pictureBox1.BeginInit()
		self._menuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# pictureBox1
		# 
		self._pictureBox1.BackColor = System.Drawing.Color.LightYellow
		self._pictureBox1.Location = System.Drawing.Point(410, 86)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(139, 128)
		self._pictureBox1.TabIndex = 0
		self._pictureBox1.TabStop = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.SkyBlue
		self._label1.Font = System.Drawing.Font("Microsoft YaHei UI", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(30, 32)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(911, 39)
		self._label1.TabIndex = 1
		self._label1.Text = "Bienvenido(a): "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SkyBlue
		self._button1.Location = System.Drawing.Point(396, 405)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(170, 44)
		self._button1.TabIndex = 2
		self._button1.Text = "Empezar"
		self._button1.UseVisualStyleBackColor = False
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(102, 263)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(800, 103)
		self._label2.TabIndex = 3
		self._label2.Text = "Control Aereo te ayudá a"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Verdana", 21.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ControlDarkDark
		self._label3.Location = System.Drawing.Point(363, 217)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(242, 46)
		self._label3.TabIndex = 4
		self._label3.Text = "Control Areo©"
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._ayudaToolStripMenuItem,
			self._salirToolStripMenuItem]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(980, 24)
		self._menuStrip1.TabIndex = 5
		self._menuStrip1.Text = "menuStrip1"
		# 
		# ayudaToolStripMenuItem
		# 
		self._ayudaToolStripMenuItem.Name = "ayudaToolStripMenuItem"
		self._ayudaToolStripMenuItem.Size = System.Drawing.Size(53, 20)
		self._ayudaToolStripMenuItem.Text = "Ayuda"
		# 
		# salirToolStripMenuItem
		# 
		self._salirToolStripMenuItem.Name = "salirToolStripMenuItem"
		self._salirToolStripMenuItem.Size = System.Drawing.Size(40, 20)
		self._salirToolStripMenuItem.Text = "salir"
		# 
		# Form1
		# 
		self.BackColor = System.Drawing.Color.AliceBlue
		self.ClientSize = System.Drawing.Size(980, 501)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._menuStrip1)
		self.Font = System.Drawing.Font("Microsoft YaHei UI", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "Form1"
		self.Text = "Usuario"
		self._pictureBox1.EndInit()
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def ToolTip1Popup(self, sender, e):
		pass