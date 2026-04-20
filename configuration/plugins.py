# Включаем плагин в список активных
PLUGINS = ['netbox_topology_views']

# Настраиваем плагин
PLUGINS_CONFIG = {
    'netbox_topology_views': {
        'static_image_directory': 'netbox_topology_views/img',
        'allow_coordinates_saving': True,
        'always_save_coordinates': False
    },
}

