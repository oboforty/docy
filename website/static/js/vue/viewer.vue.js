export const template = `
  <div>

    <form action="" method="post" id="upload_form">
       <!--  TODO: FIXME: add csrf token via js  -->
       <!-- {% csrf_token %} -->

      <fieldset v-if="patient">
        <h5>Patient #{{ patient.pid }}</h5>

        <div class="row">
          <div class="col">
            <!--<small class="required" for="id_first_name">First name:</small>-->
            <input v-model="patient.first_name" type="text" name="first_name" class="form-control" maxlength="20" required id="id_first_name" placeholder="First Name">
          </div>
          <div class="col">
            <!--<small class="required" for="id_last_name">Last name:</small>-->
            <input v-model="patient.last_name" type="text" name="last_name" class="form-control" maxlength="20" required id="id_last_name" placeholder="Last Name"><br/>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <small class="required" for="id_gender">Gender:</small>
            <select name="gender" required id="id_gender" class="form-control" v-model="patient.gender">
                <option value="" selected>Gender</option>
                <option value="1">Male</option>
                <option value="2">Female</option>
            </select>
          </div>
          <div class="col">
            <small class="required" for="id_weight">Weight:</small>
            <input type="number" name="weight" step="any" required id="id_weight" class="form-control">
          </div>
          <div class="col">
            <small class="required" for="id_birth_date">Birth date:</small>
            <input type="date" name="birth_date" class="form-control" size="10" required id="id_birth_date" placeholder="Birth Date" v-model="patient.birth_date">
          </div>
          <div class="col">
            <small class="required" for="id_age">Age:</small>
            <input type="number" name="age" class="form-control" required id="id_age" placeholder="Age" v-model="patient.age" min="1" max="130">
          </div>
        </div>
      </fieldset>

      <!-- TODO: this fieldset changes dynamically according to cancer type -->
      <fieldset v-if="patient">
        <h6>Patient details</h6>

        <div class="row">
          <div class="col">
            <div class="custom-control custom-checkbox">
              <input type="checkbox" class="custom-control-input" id="id_Chemo" v-model="patient.Chemo">
              <small class="custom-control-label" for="id_Chemo">Chemo</small>
            </div>
          </div>
          <div class="col">
            <div class="custom-control custom-checkbox">
              <input type="checkbox" class="custom-control-input" id="id_diabetes" v-model="patient.diabetes">
              <small class="custom-control-label" for="id_diabetes">Diabetes</small>
            </div>
          </div>
          <div class="col">
            <div class="custom-control custom-checkbox">
              <input type="checkbox" class="custom-control-input" id="id_insulin" v-model="patient.insulin">
              <small class="custom-control-label" for="id_insulin">Insulin</small>
            </div>
          </div>
          <div class="col">
            <div class="custom-control custom-checkbox">
              <input type="checkbox" class="custom-control-input" id="id_smoker" v-model="patient.smoker">
              <small class="custom-control-label" for="id_smoker">Smoker</small>
            </div>
          </div>
          <div class="col">
            <small class="required" for="id_Packs_yearly">Packs yearly:</small>
            <input type="number" name="Packs_yearly" class="form-control" required id="id_Packs_yearly" v-model="patient.Packs_yearly">
          </div>
          <div class="col">
            <small class="required" for="id_Last_Chemo">Last Chemo:</small>
            <input type="date" name="last_chemo" class="form-control" size="10" required id="id_Last_Chemo" placeholder="Last Chemo" v-model="patient.Last_Chemo" :disabled="!patient.Chemo">
          </div>
        </div>
      </fieldset>

      <hr />

      <fieldset v-if="scan">
        <h6>Scan #{{ scan.sid }}</h6>

        <div class="row">
          <div class="col">
          </div>
          <div class="col">
          </div>
          <div class="col">
          </div>
        </div>
      </fieldset>

    </form>

  </div>
`;