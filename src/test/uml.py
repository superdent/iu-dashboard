import matplotlib.patches as patches
import matplotlib.pyplot as plt

# Erstellung einer Skizze für das UML-Klassendiagramm als PNG

fig, ax = plt.subplots(figsize=(10, 8))

# DataManager Klasse
ax.add_patch(patches.Rectangle((1, 8), 4, 2, edgecolor='black', facecolor='lightgrey'))
ax.text(1.5, 9.5, 'DataManager', fontsize=12, fontweight='bold')

# Studium Klasse
ax.add_patch(patches.Rectangle((1, 5), 4, 2, edgecolor='black', facecolor='lightgrey'))
ax.text(1.5, 6.5, 'Studium', fontsize=12, fontweight='bold')

# Semester Klasse
ax.add_patch(patches.Rectangle((6, 5), 4, 2, edgecolor='black', facecolor='lightgrey'))
ax.text(6.5, 6.5, 'Semester', fontsize=12, fontweight='bold')

# Modul Klasse
ax.add_patch(patches.Rectangle((6, 2), 4, 2, edgecolor='black', facecolor='lightgrey'))
ax.text(6.5, 3.5, 'Modul', fontsize=12, fontweight='bold')

# Pruefung Klasse
ax.add_patch(patches.Rectangle((6, -1), 4, 2, edgecolor='black', facecolor='lightgrey'))
ax.text(6.5, 0.5, 'Pruefung', fontsize=12, fontweight='bold')

# StudiumZiel Klasse
ax.add_patch(patches.Rectangle((1, 2), 4, 2, edgecolor='black', facecolor='lightgrey'))
ax.text(1.5, 3.5, 'StudiumZiel', fontsize=12, fontweight='bold')

# Verbindungen
ax.annotate('', xy=(3, 8), xytext=(3, 7), arrowprops=dict(facecolor='black'))
ax.annotate('', xy=(3, 5), xytext=(8, 5), arrowprops=dict(facecolor='black'))
ax.annotate('', xy=(8, 5), xytext=(8, 4), arrowprops=dict(facecolor='black'))
ax.annotate('', xy=(8, 2), xytext=(8, 1), arrowprops=dict(facecolor='black'))

# Pfeil von DataManager zu Studium
ax.annotate('', xy=(3, 7), xytext=(3, 6), arrowprops=dict(facecolor='black'))

# Text hinzufügen
ax.text(4.5, 6, '1:n', fontsize=10)
ax.text(8.5, 3, '1:n', fontsize=10)
ax.text(8.5, 0, '1:n', fontsize=10)

# Diagramm-Anpassungen
ax.set_xlim(0, 12)
ax.set_ylim(-2, 12)
ax.set_axis_off()

# Diagramm speichern
plt.savefig("backend_uml_diagram.png", bbox_inches='tight')
plt.show()
