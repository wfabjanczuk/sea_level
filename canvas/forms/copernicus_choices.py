from canvas.constants import formats, hours, days, months, years, product_types
from canvas.constants.reanalysis_era5_single_levels import filters as era5_filters

years_list = []
months_list = []
days_list = []
hours_list = []
formats_list_sea_level = []
formats_list_era5 = []

for i in range(years.MIN, years.MAX + 1):
    years_list.append((i, i))

for i in range(months.MIN, months.MAX + 1):
    months_list.append((i, months.names[i - 1]))

for i in range(days.MIN, days.MAX + 1):
    days_list.append((i, i))

for i in range(hours.MIN, hours.MAX + 1):
    hours_list.append((i, "{:02d}".format(i) + ":00"))

for f in formats.list_sea_level:
    formats_list_sea_level.append((f.extension[1], f.name))

for f in formats.list_era5:
    formats_list_era5.append((f.extension[1], f.name))

product_types = tuple(product_types.product_types_list)
years = tuple(years_list)
months = tuple(months_list)
days = tuple(days_list)
hours = tuple(hours_list)
formats_sea_level = tuple(formats_list_sea_level)
formats_era5 = tuple(formats_list_era5)

categories = era5_filters.filter_categories
