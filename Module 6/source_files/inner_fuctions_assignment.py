def measurements(measurement_list):
    """
    calculates area and perimeter of rectangles/squares

    function first determines if only one value is present in measurement_list



    :param measurement_list: numeric dimensions of shape
    :return: string describing results
    """
    if len(measurement_list) == 1:
        measurement_list.append(measurement_list[0])

    def area(measurement_list):
        return float(measurement_list[0]*measurement_list[1])
    def perimeter(measurement_list):
        return float((measurement_list[0]+measurement_list[1])*2)

    return "Perimeter = " + str(perimeter(measurement_list)) + " " + "Area = " + str(area(measurement_list))


if __name__ == '__main__':
    measurements([1,2])
