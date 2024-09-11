// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HospitalManagement {

    struct Patient {
        uint id;
        string name;
        uint age;
        string medicalHistory;
        string treatment;
        uint temperature;
        uint heartRate;
    }

    uint public patientCount = 0;
    mapping(uint => Patient) public patients;

    event PatientAdded(uint id, string name, uint age, string medicalHistory, string treatment, uint temperature, uint heartRate);

    function addPatient(
        string memory _name,
        uint _age,
        string memory _medicalHistory,
        string memory _treatment,
        uint _temperature,
        uint _heartRate
    ) public {
        patientCount++;
        patients[patientCount] = Patient(patientCount, _name, _age, _medicalHistory, _treatment, _temperature, _heartRate);
        emit PatientAdded(patientCount, _name, _age, _medicalHistory, _treatment, _temperature, _heartRate);
    }

    function getPatient(uint _id) public view returns (
        uint, string memory, uint, string memory, string memory, uint, uint
    ) {
        Patient memory p = patients[_id];
        require(p.id != 0, "Patient does not exist");
        return (p.id, p.name, p.age, p.medicalHistory, p.treatment, p.temperature, p.heartRate);
    }

    function getAllPatientIds() public view returns (uint[] memory) {
        uint[] memory ids = new uint[](patientCount);
        for (uint i = 0; i < patientCount; i++) {
            ids[i] = i + 1; // IDs are 1-based
        }
        return ids;
    }
}
