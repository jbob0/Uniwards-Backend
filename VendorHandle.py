import ResponseHandle, SQLHandle

def GetVendorByID(vendor_id):
    temp_vendor = SQLHandle.vendor.query.filter_by(id=vendor_id).first()
    if(temp_vendor is not None):
        response = ResponseHandle.GenerateVendorResponse("vendor_get_success", temp_vendor.todict())
    else:
        response = ResponseHandle.GenerateResponse('vendor_get_failed')
    return response



def GetVendors():
    temp_vendors = SQLHandle.vendor.query.all()
    if (temp_vendors is not None):
        vendor_list = SQLHandle.GetListOfRows(temp_vendors)
        if (vendor_list is not None):
            if(len(vendor_list) > 0):
                response = ResponseHandle.GenerateVendorsResponse("vendor_get_success", vendor_list)
            else:
                response = ResponseHandle.GenerateResponse('vendor_get_failed')
        else:
            response = ResponseHandle.GenerateResponse('vendor_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('vendor_get_failed')

    return response


def GetVendorsByType(type):
    temp_vendors = SQLHandle.vendor.query.filter_by(type=type)
    if (temp_vendors is not None):
        vendor_list = SQLHandle.GetListOfRows(temp_vendors)
        if (vendor_list is not None):
            if(len(vendor_list) > 0):
                response = ResponseHandle.GenerateVendorsResponse("vendor_get_success", vendor_list)
            else:
                response = ResponseHandle.GenerateResponse('vendor_get_failed')
        else:
            response = ResponseHandle.GenerateResponse('vendor_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('vendor_get_failed')


    return response


def RegisterVendor(req_data):
    temp_vendor = SQLHandle.vendor(name=req_data['name'], mobile=req_data['mobile'],
                                           website=req_data['website'], type=req_data['type'],
                                           email=req_data['email'], passcode=req_data['passcode'])
    if(SQLHandle.InsertRowObject(temp_vendor)):
        response = ResponseHandle.GenerateResponse('vendor_register_success')
    else:
        response = ResponseHandle.GenerateResponse('vendor_register_failed')
    return response


def UpdateVendor(req_data):
    pass


def DeleteVendor(req_data):
    pass


def ValidateVendorPasscode(passcode, vendor_id):
    vendor = SQLHandle.vendor.query.filter_by(id=vendor_id).first()
    if(vendor is not None):
        str_passcode = str(vendor.passcode)
        if(passcode == str_passcode):
            response = ResponseHandle.GenerateResponse('passcode_success')
        else:
            response = ResponseHandle.GenerateResponse('passcode_incorrect')
    else:
        response = ResponseHandle.GenerateResponse('passcode_incorrect')

    return response

