# Autogenerated file
def render(info, hardware, dx_label, dxpin):
    yield """
   <form  method='post'>
   <table>
      <TH>Hardware Settings
      <TH>
      <TR>
         <TD>Status LED:
         <TD>
            <select name='boardled'>
               <option value=''"""
    if hardware['boardled'] == "":
        yield """ selected"""
    yield """> </option>
               """
    for cnt in range(0,dx_label["count"]):
        yield """
                    <option value='d"""
        yield str(cnt)
        yield """' """
        if hardware['d'+str(cnt)] == 8  or dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['boardled'] == 'd'+str(cnt):
            yield """ selected"""
        yield """>"""
        yield str(dx_label['d'+str(cnt)])
        yield """</option>
               """
    yield """
            </select>
      <TR>
         <TD>Inversed LED:
         <TD><input type=checkbox id='inverseled' name='inverseled'"""
    if hardware['inverseled'] == 'on':
        yield """ checked"""
    yield """>
      <TR>
         <TD colspan='2'>
            <h3>I2C Interface</h3>
      <TR>
         <TD>SDA:
         <TD>
            <select name='sda'>
               <option value=''"""
    if hardware['sda'] == "":
        yield """ selected"""
    yield """> </option>
               """
    for cnt in range(0,dx_label["count"]):
        yield """
                    <option value='d"""
        yield str(cnt)
        yield """' """
        if hardware['d'+str(cnt)] == 8  or dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['sda'] == 'd'+str(cnt):
            yield """ selected"""
        yield """>"""
        yield str(dx_label['d'+str(cnt)])
        yield """</option>
               """
    yield """
            </select>
      <TR>
         <TD>SCL:
         <TD>
            <select name='scl'>
               <option value=''"""
    if hardware['scl'] == "":
        yield """ selected"""
    yield """> </option>
               """
    for cnt in range(0,dx_label["count"]):
        yield """
                    <option value='d"""
        yield str(cnt)
        yield """' """
        if hardware['d'+str(cnt)] == 8  or dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['scl'] == 'd'+str(cnt):
            yield """ selected"""
        yield """>"""
        yield str(dx_label['d'+str(cnt)])
        yield """</option>
               """
    yield """
            </select>
      <TR>
         <TD colspan='2'>
            <h3>SPI Interface</h3>
      <TR>
         <TD>MOSI:
         <TD>
            <select name='mosi'>
               <option value=''"""
    if hardware['mosi'] == "":
        yield """ selected"""
    yield """> </option>
               """
    for cnt in range(0,dx_label["count"]):
        yield """
                    <option value='d"""
        yield str(cnt)
        yield """' """
        if hardware['d'+str(cnt)] == 8  or dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['mosi'] == 'd'+str(cnt):
            yield """ selected"""
        yield """>"""
        yield str(dx_label['d'+str(cnt)])
        yield """</option>
               """
    yield """
            </select>
      <TR>
         <TD>MISO:
         <TD>
            <select name='miso'>
               <option value=''"""
    if hardware['miso'] == "":
        yield """ selected"""
    yield """> </option>
               """
    for cnt in range(0,dx_label["count"]):
        yield """
                    <option value='d"""
        yield str(cnt)
        yield """' """
        if hardware['d'+str(cnt)] == 8  or dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['miso'] == 'd'+str(cnt):
            yield """ selected"""
        yield """>"""
        yield str(dx_label['d'+str(cnt)])
        yield """</option>
               """
    yield """
            </select>
      <TR>
         <TD>SCK:
         <TD>
            <select name='sck'>
               <option value=''"""
    if hardware['sck'] == "":
        yield """ selected"""
    yield """> </option>
               """
    for cnt in range(0,dx_label["count"]):
        yield """
                    <option value='d"""
        yield str(cnt)
        yield """' """
        if hardware['d'+str(cnt)] == 8  or dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['sck'] == 'd'+str(cnt):
            yield """ selected"""
        yield """>"""
        yield str(dx_label['d'+str(cnt)])
        yield """</option>
               """
    yield """
            </select>
      <TR>
         <TD>NSS:
         <TD>
            <select name='nss'>
               <option value=''"""
    if hardware['nss'] == "":
        yield """ selected"""
    yield """> </option>
               """
    for cnt in range(0,dx_label["count"]):
        yield """
                    <option value='d"""
        yield str(cnt)
        yield """' """
        if hardware['d'+str(cnt)] == 8  or dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['nss'] == 'd'+str(cnt):
            yield """ selected"""
        yield """>"""
        yield str(dx_label['d'+str(cnt)])
        yield """</option>
               """
    yield """
            </select>
      <TR>
         <TD colspan='2'>
            <h3>UART Interface</h3>
      <TR>
         <TD>TX:
         <TD>
            <select name='tx'>
               <option value=''"""
    if hardware['tx'] == "":
        yield """ selected"""
    yield """> </option>
               """
    for cnt in range(0,dx_label["count"]):
        yield """
                    <option value='d"""
        yield str(cnt)
        yield """' """
        if hardware['d'+str(cnt)] == 8  or dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['tx'] == 'd'+str(cnt):
            yield """ selected"""
        yield """>"""
        yield str(dx_label['d'+str(cnt)])
        yield """</option>
               """
    yield """
            </select>
      <TR>
         <TD>RX:
         <TD>
            <select name='rx'>
               <option value=''"""
    if hardware['rx'] == "":
        yield """ selected"""
    yield """> </option>
               """
    for cnt in range(0,dx_label["count"]):
        yield """
                    <option value='d"""
        yield str(cnt)
        yield """' """
        if hardware['d'+str(cnt)] == 8  or dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['rx'] == 'd'+str(cnt):
            yield """ selected"""
        yield """>"""
        yield str(dx_label['d'+str(cnt)])
        yield """</option>
               """
    yield """
            </select>
      <TR>
         <TD colspan='2'>
            <h3>Dx boot states</h3>
         """
    for cnt in range(0,dx_label["count"]):
        yield """
      <TR>
         <TD>Pin mode D"""
        yield str(cnt)
        yield """:
         <TD>
            <select name='d"""
        yield str(cnt)
        yield """'>
               <option value='0'"""
        if dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['d'+str(cnt)] == 0:
            yield """ selected"""
        yield """>Off</option>
               <option value='1'"""
        if dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['d'+str(cnt)] == 1:
            yield """ selected"""
        yield """>Input</option>
               <option value='2'"""
        if dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['d'+str(cnt)] == 2:
            yield """ selected"""
        yield """>Output Pull None</option>
               <option value='3'"""
        if dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['d'+str(cnt)] == 3:
            yield """ selected"""
        yield """>Output Pull Up</option>
               <option value='4'"""
        if dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['d'+str(cnt)] == 4:
            yield """ selected"""
        yield """>Output Pull Down</option>
               <option value='5'"""
        if dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['d'+str(cnt)] == 5:
            yield """ selected"""
        yield """>Output Open Drain</option>
               <option value='6'"""
        if dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['d'+str(cnt)] == 6:
            yield """ selected"""
        yield """>Output Alt Pull Up</option>
               <option value='7'"""
        if dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['d'+str(cnt)] == 7:
            yield """ selected"""
        yield """>Output Alt Pull Down</option>
               <option value='8'"""
        if dxpin['d'+str(cnt)] != '':
            yield """disabled"""
        if hardware['d'+str(cnt)] == 8:
            yield """ selected"""
        yield """>Disabled</option>
            </select>
          """
    yield """
      <TR>
         <TD colspan='2'>
            <hr>
      <TR>
         <TD colspan='2'><a class=\"button link\" href=\"hardware\">Close</a><input class=\"button link\" type='submit' value='Submit'>
      <TR>
         <TD>
   </table>
</form>
"""