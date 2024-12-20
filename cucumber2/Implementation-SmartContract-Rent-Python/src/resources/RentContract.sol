pragma solidity 0.8.0;

contract RentContract {
    
    address owner = msg.sender; //dono do contrato é o criador

    enum Status { Created, InEffect, SuccessfulTermination, UnsuccessfulTermination }

    struct Payment {
        int paidDay;
        uint256 month;

    }

    Status status;
    string landlord; //contratado
    string tenant;  //contratante
    string tenantAddress;

    bool localIsAvailable;
    bool waterPaid;
    bool taxesPaid;

    int contractTotalValue;
    int monthlyValue;
    int dueDay; //for each paymentm, the dueDay increases in 30 days
    uint256 monthsQuantity;
    uint256 paidMonthsQuantity;
    Payment[] payments;
    int256 penalty;

    int effectiveDay;
	int creationDay;


    constructor( string memory _landlord, string memory _tenant, string memory _tenantAddress,
                 int _contractTotalValue, int _monthlyValue, uint256 _monthsQuantity,
                 int _actualDay, int _dayToBeEffective  ) public {

    	status = Status.Created;
        landlord = _landlord;
        tenant = _tenant;
        tenantAddress = _tenantAddress;
        creationDay = _actualDay;
        effectiveDay= _dayToBeEffective;

        contractTotalValue = _contractTotalValue;
        monthlyValue = _monthlyValue;
        monthsQuantity = _monthsQuantity;
        paidMonthsQuantity = 0;
        dueDay = effectiveDay + 30;
        localIsAvailable = false;
        waterPaid = false;
        taxesPaid = false;
    }

    //SETTERS
    
  	function activate (int _actualDay) public {
        if (_actualDay >= effectiveDay) {
    	    status = Status.InEffect;
        }
    }

  	function make_payment (int _actualDay) public {
        if (_actualDay <= dueDay && status == Status.InEffect){
            paidMonthsQuantity = paidMonthsQuantity + 1;
            dueDay = dueDay + 30; //update next payment day

            Payment memory payment;
            payment.month = paidMonthsQuantity;
            payment.paidDay = _actualDay;
            payments.push(payment);

            if (paidMonthsQuantity == 12 && waterPaid && taxesPaid) {
                status = Status.SuccessfulTermination;
                localIsAvailable = true;
            } else if (paidMonthsQuantity == 12 && (!waterPaid || !taxesPaid)) {
                status = Status.UnsuccessfulTermination;
                localIsAvailable = true;
                penalty = (contractTotalValue * 10) / 100;
            }
        } else if (status == Status.InEffect) {
            status = Status.UnsuccessfulTermination;
            localIsAvailable = true;
            penalty = (contractTotalValue * 10) / 100;
        }
    }

    function make_water_payment() public {
        waterPaid = true;
    }

    function make_taxes_payment() public {
        taxesPaid = true;
    }


    //GETTERS
    
    //view significa que nao tem transacao, nao precisa minerar (nao usa gas para executar)

    function getStatus() public view returns (Status) {
        return status;
    }

    function getTenant() public view returns (string memory) {
        return tenant;
    }

    function getLandlord() public view returns (string memory) {
        return landlord;
    }

    function getTenantAddress() public view returns (string memory) {
        return tenantAddress;
    }

    function getEffectiveDay() public view returns (int) {
        return effectiveDay;
    }

    function getCreationDay() public view returns (int) {
        return creationDay;
    }

    function getContractTotalValue() public view returns (int) {
        return contractTotalValue;
    }

    function getMonthlyValue() public view returns (int) {
        return monthlyValue;
    }

    function getMonthsQuantity() public view returns (uint256) {
        return monthsQuantity;
    }

    function getPaidMonthsQuantity() public view returns (uint256) {
        return paidMonthsQuantity;
    }

    function getPaidDay (uint256 _month) public view returns (int){
        for (uint256 cont = 0; cont < paidMonthsQuantity; cont++) {
            if (payments[cont].month == _month) {
                return payments[cont].paidDay;
            }
        }
        return 0;
    }

    function getLocalIsAvailable() public view returns (bool) {
        return localIsAvailable;
    }

    function getWaterPaid() public view returns (bool) {
        return waterPaid;
    }

    function getTaxesPaid() public view returns (bool) {
        return taxesPaid;
    }

    function getPenalty() public view returns (int256) {
        return penalty;
    }

}