
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class cargarArchivos(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._label2 = System.Windows.Forms.Label()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._ayudaToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._salirToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button3 = System.Windows.Forms.Button()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._pictureBox1.BeginInit()
		self._menuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(253, 71)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(258, 49)
		self._label1.TabIndex = 0
		self._label1.Text = "Carga de archivos"
		# 
		# pictureBox1
		# 
		self._pictureBox1.Location = System.Drawing.Point(26, 71)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(202, 260)
		self._pictureBox1.TabIndex = 1
		self._pictureBox1.TabStop = False
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._label2.Location = System.Drawing.Point(253, 109)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(512, 23)
		self._label2.TabIndex = 2
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._ayudaToolStripMenuItem,
			self._salirToolStripMenuItem]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(777, 24)
		self._menuStrip1.TabIndex = 3
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
		self._salirToolStripMenuItem.Size = System.Drawing.Size(41, 20)
		self._salirToolStripMenuItem.Text = "Salir"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(367, 205)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SkyBlue
		self._button1.Location = System.Drawing.Point(253, 201)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(87, 24)
		self._button1.TabIndex = 5
		self._button1.Text = "Examinar..."
		self._button1.UseVisualStyleBackColor = False
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(253, 149)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(308, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Seleccione los archivos necesarios .cssv"
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SkyBlue
		self._button2.Location = System.Drawing.Point(253, 257)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(87, 24)
		self._button2.TabIndex = 9
		self._button2.Text = "Examinar..."
		self._button2.UseVisualStyleBackColor = False
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(367, 257)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 10
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SkyBlue
		self._button3.Location = System.Drawing.Point(253, 307)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(87, 24)
		self._button3.TabIndex = 11
		self._button3.Text = "Examinar..."
		self._button3.UseVisualStyleBackColor = False
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(367, 307)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 12
		# 
		# cargarArchivos
		# 
		self.BackColor = System.Drawing.Color.AliceBlue
		self.ClientSize = System.Drawing.Size(777, 467)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "cargarArchivos"
		self.Text = "cargarArchivos"
		self.Load += self.CargarArchivosLoad
		self._pictureBox1.EndInit()
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()


	def TrackBar1Scroll(self, sender, e):
		pass

	def CargarArchivosLoad(self, sender, e):
		pass

	def ListBox1SelectedIndexChanged(self, sender, e):
		pass