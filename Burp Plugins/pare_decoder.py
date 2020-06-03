# Burp Extension - Pareq|Pares decoder

import json

from burp import IBurpExtender
from burp import IMessageEditorTabFactory
from burp import IMessageEditorTab
from burp import IParameter
from burp import IContextMenuFactory
import urllib 
import base64
import zlib
from HTMLParser import HTMLParser


# Java imports
from javax.swing import JMenuItem
from java.util import List, ArrayList


class BurpExtender(IBurpExtender, IMessageEditorTabFactory, IContextMenuFactory):
  def registerExtenderCallbacks(self, callbacks):
    self._callbacks = callbacks
    self._helpers = callbacks.getHelpers()

    callbacks.setExtensionName('Pare_ Decoder')
    callbacks.registerMessageEditorTabFactory(self)
    callbacks.registerContextMenuFactory(self)

    return

  def createNewInstance(self, controller, editable): 
    return Pare_DecoderTab(self, controller, editable)


class Pare_DecoderTab(IMessageEditorTab):
  def __init__(self, extender, controller, editable):
    self._extender = extender
    self._helpers = extender._helpers
    self._editable = editable

    self._txtInput = extender._callbacks.createTextEditor()
    self._txtInput.setEditable(editable)

    self._3dsMagicMark = ['pareq=', 'pares=', 'name="PaRes"']

    return

  def getTabCaption(self):
    return "Pare_ Decoder"

  def getUiComponent(self):
    return self._txtInput.getComponent()

  def isEnabled(self, content, isRequest):

    if isRequest:
      r = self._helpers.analyzeRequest(content)
    else:
      r = self._helpers.analyzeResponse(content)

    msg = content[r.getBodyOffset():].tostring()
      
    if (msg.lower().find(self._3dsMagicMark[0].lower())>=0 or msg.lower().find(self._3dsMagicMark[1].lower())>=0 or msg.lower().find(self._3dsMagicMark[2].lower())>=0):
        return True
    return False

  def setMessage(self, content, isRequest):
    # Encode and view
    h = HTMLParser()
    if content is None:
      self._txtInput.setText(None)
      self._txtInput.setEditable(False)
    else:
      if isRequest:
        r = self._helpers.analyzeRequest(content)
      else:
        r = self._helpers.analyzeResponse(content)

      msg = content[r.getBodyOffset():].tostring()
      left_boundary =-1
      if msg.lower().find('pareq=')>=0:
            try:
              left_boundary=msg.lower().find('pareq=')+6
            except Exception,e:
              print ("Error: I can't find pareq= in Request")
              print e
      if msg.lower().find('pares=')>=0:
            try:
              left_boundary=msg.lower().find('pares=')+6              
            except Exception,e:
              print ("Error: I can't find pares= in Request")
              print e
      if msg.lower().find('name="pares"')>=0:
            try:
              tag_start=msg.lower().find('name="pares"')
              value_start=msg.lower().find('value="',tag_start)
              left_boundary=tag_start+(value_start-tag_start)+7
            except Exception,e:
              print ("Error: I can't find PaRes in Response")
              print e      
      if left_boundary!=-1:
        garbage = msg[:left_boundary]
        clean = msg[left_boundary:]
        right_boundary=clean.find('&')
        right_boundary=clean.find('"')
        if right_boundary==-1:
              try:
                pretty_msg = zlib.decompress(base64.b64decode(urllib.unquote(h.unescape(msg[left_boundary:])).decode('utf8')))
              except Exception, e:
                print ('Error in decode - if pare_ is final param')
                print e
        else:
              try:
                pretty_msg = zlib.decompress(base64.b64decode(urllib.unquote(h.unescape(clean[:right_boundary])).decode('utf8')))
              except Exception, e:
                print ('Error in decode - if pare_ not final param. Pare_ is: '+clean[:right_boundary])
                print e
        
        self._txtInput.setText(pretty_msg)
        self._txtInput.setEditable(self._editable)
      else:
        print('Sure this is Pareq|Pares?')
        print (msg.lower())
        return
              

    self._currentMessage = content
    return

  def getMessage(self): 
    #  Past to request from your tab
    if self._txtInput.isTextModified():
      line = self._txtInput.getText().tostring()
      try:
        data = urllib.quote_plus(base64.b64encode(zlib.compress(line,2)))
      except Exception, e:
        print e
        data = self._helpers.bytesToString(self._txtInput.getText())

      # Reconstruct request
      r = self._helpers.analyzeRequest(self._currentMessage)
      msg = self._currentMessage[r.getBodyOffset():].tostring()
      left_boundary =-1
      if msg.lower().find('pareq=')>=0:
            left_boundary=msg.lower().find('pareq=')+6
      if msg.lower().find('pares=')>=0:
            left_boundary=msg.lower().find('pares=')+6              
      if left_boundary!=-1:
        garbage = msg[:left_boundary]
        clean = msg[left_boundary:]
        right_boundary=clean.find('&')
        if right_boundary==-1:
              new_msg = garbage+data
        else:
              new_msg = garbage+data+clean[right_boundary:]
      return self._helpers.buildHttpMessage(r.getHeaders(), self._helpers.stringToBytes(new_msg))
    else:
      return self._currentMessage

  def isModified(self):
    return self._txtInput.isTextModified()

  def getSelectedData(self):
    return self._txtInput.getSelectedText()