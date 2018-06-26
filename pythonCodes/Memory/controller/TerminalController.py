#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Controller stuff here

import sys
sys.path.append('..')

from model.Process import Process
from model.Memory import Memory
from view.TerminalView import View

class CtrlMemory():

    def startMemory(self):

        def createMemory():
            #Memory size input
            resultValue = self.view.insertMemSizeMessage()

            #Verify if value is not none
            if resultValue is 0 or resultValue is None:
                self.view.programFinishMessage()
                exit()
            #Verify if value is less than 0
            elif resultValue < 0:
                self.view.incorrectValueMessage()
                self.view.tryAgainMessage()
                createMemory()
            else:
                try:
                    Memory.createMemories(self, resultValue)
                    return True
                except Exception as error:
                    self.view.failedToCreateMemoryMessage()
                    print(error)
                    self.view.programFinishMessage()
                    exit()

        self.view.programStartMessage()

        if createMemory():
            self.view.successfullyCreatedMemoryMessage()

    def insertPrograms(self):

        #Function to show memories content
        def showMemories():
            self.view.showMemoriesChosen()
            allMemoriesList = Memory.memory_List

            #Print formatted memory information
            for each in allMemoriesList:
                self.view.showMemoryInformation(each)
                data = each.memory_Data
                self.view.showFormattedMemoryOpenArray()
                for step in data:
                    self.view.showFormattedMemoryStep(step)
                self.view.showFormattedMemoryCloseArray()
            self.view.clickToContinueMessage()

        def createProcess():
            allMemoriesList = Memory.memory_List
            self.view.insertProcessChosen()

            #Returning 'name' and 'size'
            processInfo = self.view.createProcessMessage()

            #Check if dict is not null
            if processInfo != None:
                processName = processInfo['name']
                processSize = processInfo['size']

                counter = 0
                for each in allMemoriesList:
                    if processSize <= each.memory_MaxForProcess:
                        counter += 1

                if counter > 0:
                    newProcess = Process(processName, processSize)

                    for each in allMemoriesList:
                        if processSize > each.memory_MaxForProcess:
                            #print(each) Criar view depois
                            self.view.notAvailableMemoryMessage(each.memoryName())
                        else:
                            if each.memory_Id == 0:
                                #FirstFit
                                content = Memory.firstFit(each, newProcess.process_Size, newProcess.process_PID)
                                newProcess.process_Memories['First Fit'] = True
                                self.view.showFitPosition(content['fit'], content['position'])
                            elif each.memory_Id == 1:
                                #BestFit
                                content = Memory.bestFit(each, newProcess.process_Size, newProcess.process_PID)
                                newProcess.process_Memories['Best Fit'] = True
                                self.view.showFitPosition(content['fit'], content['position'])
                            elif each.memory_Id == 2:
                                #WorstFit
                                content = Memory.worstFit(each, newProcess.process_Size, newProcess.process_PID)
                                newProcess.process_Memories['Worst Fit'] = True
                                self.view.showFitPosition(content['fit'], content['position'])
                            else:
                                #CircularFit
                                content = Memory.circularFit(each, newProcess.process_Size, newProcess.process_PID)
                                newProcess.process_Memories['Circular Fit'] = True
                                self.view.showFitPosition(content['fit'], content['position'])
                else:
                    self.view.processNotCreatedMessage()

            self.view.clickToContinueMessage()


        def listProcess():
            allProcessList = Process.process_List

            if not allProcessList:
                self.view.noProcessesCreated()
                self.view.clickToContinueMessage()
                return

            self.view.listProcessChosen()

            for each in allProcessList:
                self.view.showProcesses(each, each.memoryAssociated())
            self.view.clickToContinueMessage()

        def removeProcess():
            allProcessList = Process.process_List

            if not allProcessList:
                self.view.noProcessesCreated()
                self.view.clickToContinueMessage()
                return

            self.view.removeProcessChosen()

            processId = self.view.removeProcessMessage()

            for each in allProcessList:
                if each.process_PID is processId:
                    try:
                        allMemoriesList = Memory.memory_List

                        for each2 in allMemoriesList:
                            each2.removeProcessFromMemory(processId)

                        allProcessList.remove(each)
                        self.view.processSuccessfullyRemoved(processId)
                        self.view.clickToContinueMessage()
                        return
                    except Exception as error:
                        print(error)

            self.view.processDoesntExist(processId)
            self.view.clickToContinueMessage()

        def programMenu():
            menuResultOption = self.view.menuMessage()

            if menuResultOption == 0:
                self.view.programFinishMessage()
                exit()
            elif menuResultOption < 0:
                self.view.incorrectValueMessage()
                self.view.tryAgainMessage()
                programMenu()
            elif menuResultOption == 1:
                showMemories()
            elif menuResultOption == 2:
                createProcess()
            elif menuResultOption == 3:
                removeProcess()
            else:
                listProcess()
            programMenu()

        programMenu()

    #Inicializa objeto view
    def __init__(self):
        self.view = View()
