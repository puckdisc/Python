def measurements(measurement_list):
    """


    :param measurement_list: numeric dimensions of shape
    :return: string describing results
    """

    def area(measurement_list):
        return float(measurement_list[0]*measurement_list[1])
    def perimeter(measurement_list):
        return float((measurement_list[0]+measurement_list[1])*2)

    return "Perimeter = " + str(perimeter(measurement_list)) + " " + "Area = " + str(area(measurement_list))


if __name__ == '__main__':
    measurements([1,2])
